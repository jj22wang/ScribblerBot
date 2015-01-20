<?php
	$mysqli = new mysqli("104.236.34.115","scribbler","scribbler","scribbler");

	$DestX = 2;
	$DestY = 3;
	// Check connection
	if (mysqli_connect_errno()) {
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}
	
	mysqli_query($mysqli,"INSERT INTO commandList VALUES ('2','".$DestX."','".$DestY."')");

	mysqli_close($mysqli);
?>
