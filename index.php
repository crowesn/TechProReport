<html>
<head><title>TechPro Not Yet Returned Report</title><h1>TechPro Not Yet Returned Report</h1></head> 
<body>

</body>
</html>
<?php
	//if (isset($_POST['submit']))
	if($_SERVER['REQUEST_METHOD'] == 'POST') 
	{
		$login = $_POST['login'];
		$pass = $_POST['pass'];
		$email = $_POST['email'];
		//passthru('(/usr/bin/python /Volumes/UCFSsan32/Groups/ulib/EResources/Sites/PyTest/test.py '.$login.' '.$pass.') 2>&1');
		passthru('(/usr/bin/python /Volumes/UCFSsan32/Groups/ulib/EResources/Sites/TechProReport/TechProWebForm.py '.$login.' '.$pass.' '.$email.') 2>&1');
		//Destroy the session. 
		session_destroy();
	}
	else
	{
	echo "<p>Enter credentials below to queue a report of TechPro items in UCLID that are outstanding.<br>The report will be delivered via email.</p><form method=\"post\"><table border=0><tr><td>Email :</td><td> <input type=\"text\" name=\"email\"></td></tr><tr><td>Login: </td><td><input type=\"text\" name=\"login\"></td></tr><tr><td>Password: </td><td><input type=\"password\" name=\"pass\"></td></tr></table><p><button name=\"submit\">Run Report</button></p></form>";
	}
?>
