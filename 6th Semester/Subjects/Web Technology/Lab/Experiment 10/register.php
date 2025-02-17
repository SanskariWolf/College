<?php

// Define the file path where user credentials are stored
$users_file = "users.txt"; // IMPORTANT: Make sure this file is NOT web-accessible!

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $confirm_password = $_POST["confirm_password"];

    // Validate input (more thorough validation is needed in a real application)
    if (empty($username) || empty($password) || empty($confirm_password)) {
        $error_message = "All fields are required.";
    } elseif ($password !== $confirm_password) {
        $error_message = "Passwords do not match.";
    } else {
        // Hash the password
        $hashed_password = password_hash($password, PASSWORD_DEFAULT);

        // Store the username and hashed password in the file
        $user_data = $username . ":" . $hashed_password . PHP_EOL;

        // Use LOCK_EX to prevent race conditions during file writing
        if (file_put_contents($users_file, $user_data, FILE_APPEND | LOCK_EX) !== false) {
            $success_message = "Registration successful! <a href='login.php'>Login here</a>";
        } else {
            $error_message = "Error registering user.  Please try again.";
        }
    }
}

?>

<!DOCTYPE html>
<html>

<head>
    <title>Register</title>
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

        .register-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }

        .register-container h2 {
            text-align: center;
            margin-bottom: 20px;
            color: #333;
        }

        .register-container input[type="text"],
        .register-container input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        .register-container input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }

        .register-container input[type="submit"]:hover {
            background-color: #45a049;
        }

        .error-message {
            color: red;
            margin-bottom: 10px;
        }

        .success-message {
            color: green;
            margin-bottom: 10px;
        }
    </style>
</head>

<body>

    <div class="register-container">
        <h2>Register</h2>

        <?php if (isset($error_message)): ?>
            <p class="error-message"><?php echo $error_message; ?></p>
        <?php endif; ?>

        <?php if (isset($success_message)): ?>
            <p class="success-message"><?php echo $success_message; ?></p>
        <?php endif; ?>


        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username" required><br><br>

            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" required><br><br>

            <label for="confirm_password">Confirm Password:</label><br>
            <input type="password" id="confirm_password" name="confirm_password" required><br><br>

            <input type="submit" value="Register">
        </form>

        <p>Already have an account? <a href="login.php">Login here</a></p>

    </div>

</body>

</html>