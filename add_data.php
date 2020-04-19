<?php
        include("connect.php");
        $dateS = date('m/d/Y h:i:s',time());
        date_default_timezone_set('America/New_York');
        $SQL = "INSERT INTO LoggedInfodb.tbl_Probes(MAC_Address, SSID, Location, Time) VALUES ('".$_GET["MAC"]."','".$_GET["SSID"]."','".$_GET["Location"]."','$dateS')";
        echo $SQL;
        mysqli_query($conn,$SQL);
?>
