<?php

// -----------------------------------  display.php  -----------------------------------

try {
    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // SQL query to select all users
    $sql = "SELECT id, name, address, email, mobile FROM users";
    $result = $conn->query($sql);

} catch (Exception $e) {
    die("Error: " . $e->getMessage());
}

?>

<!DOCTYPE html>
<html>

<head>
    <title>User List</title>
    <style>
        body {
            font-family: sans-serif;
        }

        table {
            border-collapse: collapse;
            width: 100%;
        }

        th,
        td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }
    </style>
</head>

<body>

    <h2>User List</h2>

    <?php
    if (isset($result) && $result->num_rows > 0) {
        echo "<table>";
        echo "<tr><th>ID</th><th>Name</th><th>Address</th><th>Email</th><th>Mobile</th></tr>";

        // Output data of each row
        while ($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . $row["id"] . "</td>";
            echo "<td>" . $row["name"] . "</td>";
            echo "<td>" . $row["address"] . "</td>";
            echo "<td>" . $row["email"] . "</td>";
            echo "<td>" . $row["mobile"] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "No users found.";
    }

    //Close connection
    if (isset($conn)) {
        $conn->close();
    }
    ?>

</body>

</html>