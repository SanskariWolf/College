<!DOCTYPE html>
<html>

<head>
  <title>Data from Text File</title>
  <style>
    table {
      border-collapse: collapse;
      width: 80%;
      margin: 20px auto;
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

  <?php

  $filename = "data.txt";

  if (file_exists($filename)) {
    $file = fopen($filename, "r");

    if ($file) {
      echo "<table>";
      echo "<thead><tr><th>Name</th><th>Password</th><th>Email</th></tr></thead>";
      echo "<tbody>";

      while (($line = fgets($file)) !== false) {
        $parts = explode(":", $line);

        if (count($parts) === 3) {
          $name = trim($parts[0]);
          $password = trim($parts[1]);
          $email = trim($parts[2]);

          echo "<tr>";
          echo "<td>" . htmlspecialchars($name) . "</td>";
          echo "<td>" . htmlspecialchars($password) . "</td>";
          echo "<td>" . htmlspecialchars($email) . "</td>";
          echo "</tr>";
        } else {
          echo "<tr><td colspan='3'>Invalid data format in file: " . htmlspecialchars($line) . "</td></tr>";
        }
      }

      echo "</tbody>";
      echo "</table>";

      fclose($file);
    } else {
      echo "Error opening file: " . $filename;
    }
  } else {
    echo "File not found: " . $filename;
  }

  ?>

</body>

</html>