<?php
$conn = new mysqli("localhost", "root", "3mm@hNj3r!", "users");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} else {
    echo "Connection successful!";
}
?>