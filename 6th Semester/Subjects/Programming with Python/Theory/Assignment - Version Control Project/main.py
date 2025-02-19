import os
import shutil
import hashlib
import time
import datetime
import configparser
import difflib
import uuid


class SVCS:
    def __init__(self):
        self.project_dir = None
        self.svcs_dir = None
        self.config_file = None
        self.index_file = None
        self.versions_dir = None
        self.config = None
        self.username = None
        self.ignored_files = None

    def display_menu(self):
        self.load_project_from_config()  # Try to load project on startup
        while True:
            print("\nSVCS Menu:")
            print("1. Initialize project")
            print("2. Add item")
            print("3. Create version")
            print("4. List versions")
            print("5. Restore version")
            print("6. Show diff")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                project_dir = input("Enter project directory: ")
                self.initialize_project(project_dir)
            elif choice == '2':
                if not self.project_dir:
                    print("Error: Project not initialized. Please initialize a project first.")
                    continue
                item_path = input("Enter item path (relative to project directory): ")
                self.add_item(self.project_dir, item_path)
            elif choice == '3':
                if not self.project_dir:
                    print("Error: Project not initialized. Please initialize a project first.")
                    continue
                commit_message = input("Enter commit message: ")
                self.create_version(self.project_dir, commit_message)
            elif choice == '4':
                if not self.project_dir:
                    print("Error: Project not initialized. Please initialize a project first.")
                    continue
                self.list_versions(self.project_dir)
            elif choice == '5':
                if not self.project_dir:
                    print("Error: Project not initialized. Please initialize a project first.")
                    continue
                version = input("Enter version to restore: ")
                self.restore_version(self.project_dir, version)
            elif choice == '6':
                if not self.project_dir:
                    print("Error: Project not initialized. Please initialize a project first.")
                    continue
                version1 = input("Enter first version: ")
                version2 = input("Enter second version: ")
                self.show_diff(self.project_dir, version1, version2)
            elif choice == '7':
                print("Exiting SVCS.")
                break
            else:
                print("Invalid choice. Please try again.")

    def initialize_project(self, project_dir):
        self.project_dir = project_dir
        self.svcs_dir = os.path.join(self.project_dir, ".svcs")
        self.config_file = os.path.join(self.svcs_dir, "config.txt")
        self.index_file = os.path.join(self.svcs_dir, "index.txt")
        self.versions_dir = os.path.join(self.svcs_dir, "versions")

        try:
            os.makedirs(self.svcs_dir, exist_ok=True)
            os.makedirs(self.versions_dir, exist_ok=True)

            self.config = configparser.ConfigParser()
            self.config['user'] = {'username': input("Enter your username: ")}
            self.config['ignore'] = {'files': ''}
            self.config['project'] = {'project_dir': self.project_dir} # Save project directory

            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)

            open(self.index_file, 'w').close()  # Create an empty index file

            self.load_config()

            print(f"Project initialized in {self.project_dir}")

        except Exception as e:
            print(f"Error initializing project: {e}")
            self.project_dir = None
            self.svcs_dir = None
            self.config_file = None
            self.index_file = None
            self.versions_dir = None
            self.config = None
            self.username = None
            self.ignored_files = None

    def load_config(self):
        if not self.project_dir:
            print("Error: Project not initialized. Please initialize a project first.")
            return

        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)
        self.username = self.config['user']['username']
        self.ignored_files = self.config['ignore']['files'].split(',')
        self.ignored_files = [f.strip() for f in self.ignored_files if f.strip()]

    def is_ignored(self, item_path):
        for ignored_file in self.ignored_files:
            if item_path == ignored_file or item_path.startswith(ignored_file + '/'):
                return True
        return False

    def add_item(self, project_dir, item_path):
        if not self.project_dir:
            print("Error: Project not initialized. Please initialize a project first.")
            return

        full_path = os.path.join(project_dir, item_path)

        if not os.path.exists(full_path):
            print(f"Error: Item '{item_path}' not found.")
            return

        if self.is_ignored(item_path):
            print(f"Skipping ignored file: {item_path}")
            return

        try:
            with open(self.index_file, 'a') as index_file:
                if os.path.isfile(full_path):
                    sha256_hash = self.calculate_sha256(full_path)
                    index_file.write(f"{item_path},{sha256_hash}\n")
                    print(f"Added file '{item_path}' to version control.")
                elif os.path.isdir(full_path):
                    for root, _, files in os.walk(full_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            relative_path = os.path.relpath(file_path, project_dir)

                            if self.is_ignored(relative_path):
                                print(f"Skipping ignored file: {relative_path}")
                                continue

                            sha256_hash = self.calculate_sha256(file_path)
                            index_file.write(f"{relative_path},{sha256_hash}\n")
                            print(f"Added file '{relative_path}' to version control.")
                else:
                    print(f"Error: Item '{item_path}' is not a file or directory.")

        except Exception as e:
            print(f"Error adding item: {e}")

    def calculate_sha256(self, file_path):
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()

    def create_version(self, project_dir, commit_message):
        if not self.project_dir:
            print("Error: Project not initialized. Please initialize a project first.")
            return

        try:
            version_number = self.get_next_version_number()
            version_dir = os.path.join(self.versions_dir, f"v{version_number}")
            os.makedirs(version_dir)

            version_files_dir = os.path.join(version_dir, "files")
            os.makedirs(version_files_dir)

            index_data = self.read_index_file()
            file_hashes = []

            # Dictionary to store unique files by their hash
            unique_files = {}

            for item_path, sha256_hash in index_data:
                source_path = os.path.join(project_dir, item_path)
                dest_path = os.path.join(version_files_dir, item_path)

                # Create directory structure in version folder
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                if sha256_hash in unique_files:
                    # Use hard link if the file content is the same
                    try:
                        os.link(unique_files[sha256_hash], dest_path)
                        print(f"Hardlinked: {item_path}")
                    except OSError as e:
                        # Handle cases where hard linking might fail (e.g., cross-device linking)
                        print(f"Hardlink failed for {item_path}: {e}. Copying instead.")
                        shutil.copy2(source_path, dest_path)
                        unique_files[sha256_hash] = dest_path


                else:
                    # Copy the file if it is not a duplicate
                    shutil.copy2(source_path, dest_path)  # copy2 preserves metadata
                    unique_files[sha256_hash] = dest_path
                    print(f"Copied: {item_path}")

                file_hashes.append(sha256_hash)

            self.write_version_history(version_dir, commit_message, file_hashes)
            print(f"Created version v{version_number}")

        except Exception as e:
            print(f"Error creating version: {e}")

    def get_next_version_number(self):
        version_numbers = []
        try:
            for entry in os.listdir(self.versions_dir):
                if entry.startswith('v') and os.path.isdir(os.path.join(self.versions_dir, entry)):
                    try:
                        version_number = int(entry[1:])
                        version_numbers.append(version_number)
                    except ValueError:
                        pass  # Ignore directories that don't follow the 'v[number]' format
        except FileNotFoundError:
            return 1
        if version_numbers:
            return max(version_numbers) + 1
        else:
            return 1

    def read_index_file(self):
        index_data = []
        try:
            with open(self.index_file, 'r') as index_file:
                for line in index_file:
                    item_path, sha256_hash = line.strip().split(',', 1)
                    index_data.append((item_path, sha256_hash))
        except FileNotFoundError:
            print("Index file not found.")
            return []
        return index_data

    def write_version_history(self, version_dir, commit_message, file_hashes):
        history_file = os.path.join(version_dir, "history.txt")
        timestamp = datetime.datetime.now().isoformat()
        try:
            with open(history_file, 'w') as f:
                f.write(f"Commit Message: {commit_message}\n")
                f.write(f"Timestamp: {timestamp}\n")
                f.write(f"Username: {self.username}\n")
                f.write(f"File Hashes: {','.join(file_hashes)}\n")
        except Exception as e:
            print(f"Error writing version history: {e}")

    def list_versions(self, project_dir):
        if not self.project_dir:
            print("Error: Project not initialized. Please initialize a project first.")
            return

        try:
            versions = sorted([d for d in os.listdir(self.versions_dir) if os.path.isdir(os.path.join(self.versions_dir, d)) and d.startswith('v')])
            if not versions:
                print("No versions found.")
                return

            print("\nAvailable Versions:")
            for version in versions:
                history_file = os.path.join(self.versions_dir, version, "history.txt")
                try:
                    with open(history_file, 'r') as f:
                        lines = f.readlines()
                        commit_message = lines[0].split(': ', 1)[1].strip() if len(lines) > 0 else "No commit message"
                        timestamp = lines[1].split(': ', 1)[1].strip() if len(lines) > 1 else "No timestamp"
                        username = lines[2].split(': ', 1)[1].strip() if len(lines) > 2 else "No username"

                        print(f"Version: {version}")
                        print(f"  Commit Message: {commit_message}")
                        print(f"  Timestamp: {timestamp}")
                        print(f"  Username: {username}")
                        print("")

                except FileNotFoundError:
                    print(f"Error: History file not found for version {version}")
                except IndexError:
                    print(f"Error: Could not read history file for version {version}")

        except FileNotFoundError:
            print("Error: Versions directory not found.")
        except Exception as e:
            print(f"Error listing versions: {e}")

    def restore_version(self, project_dir, version):
        if not self.project_dir:
            print("Error: Project not initialized. Please initialize a project first.")
            return

        version_dir = os.path.join(self.versions_dir, version, "files")
        if not os.path.exists(version_dir):
            print(f"Error: Version '{version}' not found.")
            return

        try:
            # Remove all files and directories in the project directory (except .svcs)
            for item in os.listdir(project_dir):
                item_path = os.path.join(project_dir, item)
                if item != ".svcs":
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.unlink(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)

            # Copy files from the specified version to the project directory
            for root, _, files in os.walk(version_dir):
                for file in files:
                    source_path = os.path.join(root, file)
                    relative_path = os.path.relpath(source_path, version_dir)
                    dest_path = os.path.join(project_dir, relative_path)

                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.copy2(source_path, dest_path)  # Preserves metadata

            print(f"Project restored to version '{version}'.")

        except Exception as e:
            print(f"Error restoring version: {e}")

    def show_diff(self, project_dir, version1, version2):
        if not self.project_dir:
            print("Error: Project not initialized. Please initialize a project first.")
            return

        version1_dir = os.path.join(self.versions_dir, f"v{version1}", "files")
        version2_dir = os.path.join(self.versions_dir, f"v{version2}", "files")

        if not os.path.exists(version1_dir):
            print(f"Error: Version '{version1}' not found.")
            return

        if not os.path.exists(version2_dir):
            print(f"Error: Version '{version2}' not found.")
            return

        files1 = set()
        for root, _, files in os.walk(version1_dir):
            for file in files:
                files1.add(os.path.relpath(os.path.join(root, file), version1_dir))

        files2 = set()
        for root, _, files in os.walk(version2_dir):
            for file in files:
                files2.add(os.path.relpath(os.path.join(root, file), version2_dir))

        common_files = files1.intersection(files2)

        for file in sorted(common_files):
            file1_path = os.path.join(version1_dir, file)
            file2_path = os.path.join(version2_dir, file)

            print(f"\nDiff for file: {file}")

            try:
                with open(file1_path, 'r') as f1:
                    lines1 = f1.readlines()
                with open(file2_path, 'r') as f2:
                    lines2 = f2.readlines()

                diff = difflib.Differ().compare(lines1, lines2)

                for line in diff:
                    if line.startswith('  '):
                        print(f"  {line}", end='')
                    elif line.startswith('+ '):
                        print(f"+ {line}", end='')
                    elif line.startswith('- '):
                        print(f"- {line}", end='')
                    elif line.startswith('? '):
                        print(f"? {line}", end='')

            except Exception as e:
                print(f"Error diffing file {file}: {e}")

        # Report files only in version1
        only_in_v1 = files1 - files2
        if only_in_v1:
            print("\nFiles only in version {}:".format(version1))
            for file in sorted(only_in_v1):
                print("- {}".format(file))

        # Report files only in version2
        only_in_v2 = files2 - files1
        if only_in_v2:
            print("\nFiles only in version {}:".format(version2))
            for file in sorted(only_in_v2):
                print("+ {}".format(file))

    def load_project_from_config(self):
         # Try to load the project directory from the config file in the current directory or parent directories.
        current_dir = os.getcwd()
        while True:
            config_file_path = os.path.join(current_dir, ".svcs", "config.txt")
            if os.path.exists(config_file_path):
                try:
                    config = configparser.ConfigParser()
                    config.read(config_file_path)
                    project_dir = config['project']['project_dir']
                    if os.path.exists(os.path.join(current_dir, ".svcs")):
                      self.project_dir = project_dir
                      self.svcs_dir = os.path.join(self.project_dir, ".svcs")
                      self.config_file = os.path.join(self.svcs_dir, "config.txt")
                      self.index_file = os.path.join(self.svcs_dir, "index.txt")
                      self.versions_dir = os.path.join(self.svcs_dir, "versions")
                      self.config = config
                      self.username = self.config['user']['username']
                      self.ignored_files = self.config['ignore']['files'].split(',')
                      self.ignored_files = [f.strip() for f in self.ignored_files if f.strip()]
                      print(f"Project loaded from {project_dir}")
                      return
                except Exception as e:
                    print(f"Error loading project from config: {e}")
                    return
            parent_dir = os.path.dirname(current_dir)
            if parent_dir == current_dir:
                # Reached the root directory
                break
            current_dir = parent_dir


if __name__ == "__main__":
    svcs = SVCS()
    svcs.display_menu()