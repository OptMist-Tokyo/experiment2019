<html>
<head>
<link rel="stylesheet" href="css/bootstrap.css">
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script type="text/javascript" src="js/bootstrap.js"></script>
<meta http-equiv="Content-Type" charset="utf-8">
<meta http-equiv="Content-Script-Type" content="text/javascript">
<title>さくさくラズベリーパイを焼こう！</title>
<style>
body{
  background-image: url(sakusaku_pie.jpg);
  background-size: cover;
}
form{
  margin-left: 20px;
  margin-top: 10px;
}
</style>
<script type="text/javascript">
  function BackTo(){
     location.href = "raspie_sakusaku.html";
  }
</script>
</head>
<body>
<p>
<?php
putenv('/usr/local/lib/python3.5/dist-packages/');
if (is_uploaded_file($_FILES["upfile"]["tmp_name"])) {
  if ($_POST["lastname"]!="" && $_POST["firstname"]!=""){
    $newname = $_POST["lastname"] . "_" . $_POST["firstname"];
    $ext = "." . substr($_FILES["upfile"]["name"], strrpos($_FILES["upfile"]["name"], ".") + 1);
    $db_path = "/home/pi/workspace/software/db/";
    if (move_uploaded_file($_FILES["upfile"]["tmp_name"], $db_path . $_FILES["upfile"]["name"])) {
      chmod($db_path . $_FILES["upfile"]["name"], 0644);
      rename($db_path . $_FILES["upfile"]["name"], $db_path . $newname . $ext);
      //$command = '/bin/sh /home/pi/workspace/facerecognition/update.sh';
      $command = '/usr/bin/python3 /home/pi/workspace/facerecognition/collection.py';
      exec($command, $result, $judge);
      //print_r($result);
      //echo $judge;
      echo "<script>alert('画像をアップロードしました！')</script>";
    } else {
      echo "<script>alert('ファイルをアップロードできません。');</script>";
    }
  } else {
    echo "<script>alert('名前が入力されていません。');</script>";
  }
} else {
    echo "<script>alert('ファイルが選択されていません。');</script>";
}
echo "<script>BackTo();</script>";
?>
</p>
<form>
  <input type="button" value="戻る" onclick="BackTo()">
</form>
</body>
</html>
