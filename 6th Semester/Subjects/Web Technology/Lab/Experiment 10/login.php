<?php
session_start(); // Start the session

// Define the file path where user credentials are stored
$users_file = "users.txt"; // IMPORTANT: Make sure this file is NOT web-accessible!

// Function to verify login credentials
function verify_login($username, $password, $users_file)
{
    if (file_exists($users_file)) {
        $lines = file($users_file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

        foreach ($lines as $line) {
            list($stored_username, $stored_password) = explode(":", $line, 2);  // Limit explode to 2 parts
            // Always use password_verify() for checking passwords, not direct comparison
            if ($username === $stored_username && password_verify($password, $stored_password)) {
                return true; // Login successful
            }
        }
    }
    return false; // Login failed
}


// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Validate input (basic example - you should do more thorough validation)
    if (empty($username) || empty($password)) {
        $error_message = "Username and password are required.";
    } else {
        // Attempt to verify login
        if (verify_login($username, $password, $users_file)) {
            // Set session variables upon successful login
            $_SESSION["loggedin"] = true;
            $_SESSION["username"] = $username;  // Store username in session

            // Redirect to a protected page (e.g., "welcome.php")
            header("Location: welcome.php");
            exit(); // Make sure to exit after redirecting
        } else {
            $error_message = "Invalid username or password.";
        }
    }
}


?>

<!DOCTYPE html>
<html>

<head>
    <title>Login</title>
    <style>
        body {
            font-family: sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }

        .login-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }

        .login-container h2 {
            text-align: center;
            margin-bottom: 20px;
            color: #333;
        }

        .login-container input[type="text"],
        .login-container input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        .login-container input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }

        .login-container input[type="submit"]:hover {
            background-color: #45a049;
        }

        .error-message {
            color: red;
            margin-bottom: 10px;
        }
    </style>
</head>

<body>

    <div class="login-container">
        <h2>Login</h2>

        <?php if (isset($error_message)): ?>
            <p class="error-message"><?php echo $error_message; ?></p>
        <?php endif; ?>

        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username" required><br><br>

            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" required><br><br>

            <input type="submit" value="Login">
        </form>

        <p>Don't have an account? <a href="register.php">Register here</a></p>

    </div>

</body>

</html>