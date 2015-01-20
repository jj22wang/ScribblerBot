<?php
	$mysqli = new mysqli("104.236.34.115","scribbler","scribbler","scribbler");

	//$DestX = $_POST['DestX'];
	//$DestY = $_POST['DestY'];
	// Check connection
	if (mysqli_connect_errno()) {
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}
	
	$r=mysqli_query($mysqli,"SELECT MIN(commandID) FROM commandList");
	$row = mysqli_fetch_array($r);
	//var_dump($row);
	$cID=$row['MIN(commandID)'];
	$d=mysqli_query($mysqli,"SELECT * FROM commandList WHERE ".$cID."=commandID");
	$d2 = mysqli_fetch_array($d);
	
	$data=array();
	$data['DestX']=$d2['DestX'];
	$data['DestY']=$d2['DestY'];
	//print $data['DestX']." ".$data['DestY'];
	echo json_encode($data);
	mysqli_query($mysqli,"DELETE FROM commandList WHERE ".$cID."=commandID");
	mysqli_close($mysqli);
?>