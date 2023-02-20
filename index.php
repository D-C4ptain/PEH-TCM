
https://www.scip.ch/en/?labs.20171214  DOM based xss
https://xss-game.appspot.com/

<?php
$username = $_GET['username'];
echo "Hello $username";

?>

index.php?username=cap
Hello cap

index.php?username=<script>alert('Hello')</script>

cookies
