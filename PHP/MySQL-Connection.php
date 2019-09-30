<?php
# Using MySQLi from https://www.w3schools.com/php/php_mysql_connect.asp
$servername = "localhost";
$username = "test";
$password = "password";
$database = "testQueries";


$conn = new mysqli($servername, $username, $password, $database);

if($conn->connect_error){
	die("Connection failed: ". $conn->connect_error);
}

// $sql = "CREATE DATABASE testQueries";
// if($conn->query($sql) === TRUE) {
// 	echo "Database Created Successfully";
// } else {
// 	echo "Error creating database: " . $conn->error;
// }

// $sql = "CREATE TABLE testTable ( 
// 	id INT(6) PRIMARY KEY, 
// 	value INT(6)
// )";
// if($conn->query($sql) === TRUE) {
// 	echo "Success in Creating table";
// } else {
// 	echo "Error in Creating table" . $conn->error;
// }


$sql = "select * from testTable"; 
$result=$conn->query($sql);

if($result->num_rows > 0){
	while($row = $result->fetch_assoc()) {
		echo "id: " . $row["id"]. ", Value: " . $row["value"]. "\n";
	}
}


$conn->close();
?>
