<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true) {
    // Redirect to login page if not logged in
    header("Location: login.php");
    exit();
}

// Get the username from the session
$username = $_SESSION["username"];
?>

<!DOCTYPE html>
<html>

<head>
    <title>Welcome</title>
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

        .welcome-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
            text-align: center;
        }

        .welcome-container h2 {
            color: #333;
        }

        .welcome-container p {
            margin-bottom: 20px;
        }

        .welcome-container a {
            text-decoration: none;
            color: #007bff;
        }
    </style>
</head>

<body>

    <div class="welcome-container">
        <h2>Welcome, <?php echo htmlspecialchars($username); ?>!</h2>
        <p>You are now logged in.</p>
        <a href="logout.php">Logout</a>
    </div>

</body>

</html>