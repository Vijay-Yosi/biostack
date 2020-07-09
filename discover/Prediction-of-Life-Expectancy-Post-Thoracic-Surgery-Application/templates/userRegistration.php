<?php include('server.php');?>
<!DOCTYPE HTML>
<html>
<head>
	<title>User Registration</title>
	<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
	<script src="https://cdn.jsdelivr.net/jquery/1.12.4/jquery.min.js"></script>
	<script src="https://cdn.jsdelivr.net/jquery.validation/1.15.1/jquery.validate.min.js"></script>
	<script src="JS/form-validation.js"></script>
	<!-- <style type="text/css">
		body {
      background: url("https://i1.wp.com/www.globaltrademag.com/wp-content/uploads/2019/08/shutterstock_1092234560.jpg?fit=757%2C393&ssl=1") no-repeat center;
      background-size: cover;
      }
	</style> -->
</head>
<body>
	<div class="w3-container w3-center w3-padding-large">
		<div class="w3-card w3-shadow w3-center w3-third w3-padding-large" style="margin-left: 33.33%; margin-top: 4%;">
			<h3><b>User Registration</b></h3>
			<center>
			<hr style="width: 55%;">
			<form method="post" action="userRegistration.php" id = "Registration">
			<?php include('errors.php');?>
			<!-- form begins-->
			
			<label class="w3-text" required>Full Name*</label>
  			<input class="w3-input w3-border w3-margin-top w3-hover-border-teal" style="width: 80%;" name="username" id="username"  type="text" required></p>
  			
  			
  			<label class="w3-text" required>E-mail*</label>
  			<input class="w3-input w3-border w3-margin-top w3-hover-border-teal" style="width: 80%;" name="email" id="email"  type="text" required></p>
  			
  			
  			<label class="w3-text" required>Password*</label>
  			<input class="w3-input w3-border w3-margin-top w3-hover-border-teal" style="width: 80%;" name="pass" id="pass" type="password" required></p>
  			
  			
  			<label class="w3-text" required>Confirm Password*</label>
  			<input class="w3-input w3-border w3-margin-top w3-hover-border-teal" style="width: 80%;" name="confpass" id="confpass" type="password" required></p>
			<input type="submit" class="w3-btn w3-black" name="form1" value="Register">  			
  			</center>
			<p>Already registered? <a class="w3-text-teal" href="{{ url_for('login') }}" style="text-decoration: none;">Login.</a></p>
			</form>
		</div>
  	</div>
</body>
</html>
