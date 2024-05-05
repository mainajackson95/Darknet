<?php
$servername = "localhost";
$username = "root";
$password = "3mm@hNj3r!";
$dbname = "users";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check if connection is successful
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if form data is posted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Get the alias and password from the form
    $alias = $_POST['alias'];
    $password_plain = $_POST['password'];

    // Hash the password using bcrypt
    $password_hashed = password_hash($password_plain, PASSWORD_BCRYPT);

    // Prepare the SQL query to insert the user into the database
    $sql = "INSERT INTO user_info (alias, password, is_admin) VALUES (?, ?, ?)";

    // Prepare and execute the query
    $is_admin = 0;
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ssi", $alias, $password_hashed, $is_admin);

    if ($stmt->execute()) {
        // Registration successful, redirect to 'pay.html'
        header("Location: pay.html");  // Redirect to 'pay.html'
        exit();  // Ensure no further code is executed
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement and connection
    $stmt->close();
    $conn->close();
}
?>