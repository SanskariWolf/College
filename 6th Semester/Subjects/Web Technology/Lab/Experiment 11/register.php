<?php

// Database Configuration (adjust these to your settings)
$servername = "localhost";
$username = "your_mysql_username"; // Replace with your MySQL username
$password = "your_mysql_password"; // Replace with your MySQL password
$dbname = "your_database_name"; // Replace with your database name

// -----------------------------------  register.php  -----------------------------------

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Collect form data
    $name = $_POST["name"];
    $address = $_POST["address"];
    $email = $_POST["email"];
    $mobile = $_POST["mobile"];

    // Validate data (basic validation, expand as needed)
    if (empty($name) || empty($address) || empty($email) || empty($mobile)) {
        $error_message = "All fields are required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error_message = "Invalid email format.";
    } else {

        try {
            // Create connection
            $conn = new mysqli($servername, $username, $password, $dbname);

            // Check connection
            if ($conn->connect_error) {
                die("Connection failed: " . $conn->connect_error);
            }

            // Prepare and bind SQL statement (to prevent SQL injection)
            $stmt = $conn->prepare("INSERT INTO users (name, address, email, mobile) VALUES (?, ?, ?, ?)");
            $stmt->bind_param("ssss", $name, $address, $email, $mobile); // ssss indicates four string parameters

            // Execute the statement
            if ($stmt->execute() === TRUE) {
                $success_message = "User registered successfully!";
            } else {
                $error_message = "Error: " . $stmt->error;
            }

            // Close connection
            $stmt->close();
            $conn->close();

        } catch (Exception $e) {
            $error_message = "Error: " . $e->getMessage();
        }
    }
}
?>

<!DOCTYPE html>
<html>

<head>
    <title>User Registration</title>
    <style>
        body {
            font-family: sans-serif;
        }

        .error {
            color: red;
        }

        .success {
            color: green;
        }

        label {
            display: block;
            margin-top: 10px;
        }

        input[type="text"],
        textarea {
            width: 300px;
            padding: 5px;
            margin-bottom: 10px;
        }

        input[type="submit"] {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #3e8e41;
        }
    </style>
</head>

<body>

    <h2>User Registration</h2>

    <?php if (isset($error_message)): ?>
        <p class="error"><?php echo $error_message; ?></p>
    <?php endif; ?>

    <?php if (isset($success_message)): ?>
        <p class="success"><?php echo $success_message; ?></p>
    <?php endif; ?>

    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name"><br>

        <label for="address">Address:</label>
        <textarea name="address" id="address"></textarea><br>

        <label for="email">Email:</label>
        <input type="text" name="email" id="email"><br>

        <label for="mobile">Mobile No.:</label>
        <input type="text" name="mobile" id="mobile"><br>

        <input type="submit" value="Register">
    </form>

</body>

</html>