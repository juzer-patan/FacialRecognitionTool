provider "aws"{
	region = "ap-south-1"
	profile = "juzer"

}

resource "aws_instance" "myin" {
	ami           = "ami-0ad704c126371a549"
	instance_type = "t2.micro"
	key_name = "mykey111"
	security_groups = ["launch-wizard-2"]

	tags = {
		Name = "TestOs"
  }
	connection {
    type     = "ssh"
    user     = "ec2-user"
    private_key = file("C:/Users/juzer/Desktop/mykey111.pem")
    host     = aws_instance.myin.public_ip
  }
	provisioner "remote-exec" {
    inline = [
      "sudo yum install httpd php git -y",
      "sudo systemctl start httpd",
      "sudo systemctl enable httpd"	
    ]
  }
}


resource "aws_ebs_volume" "ebs2" {
  
	
  availability_zone = aws_instance.myin.availability_zone
  size              = 1

  tags = {
    Name = "Testvol"
  }
}

resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdf"
  volume_id   = aws_ebs_volume.ebs2.id
  instance_id = aws_instance.myin.id
  force_detach = true
}
output "myaz"{
	value = aws_instance.myin.availability_zone
}
output "myebsid"{
	value = aws_ebs_volume.ebs2.id
}
output "myin_id"{
	value = aws_instance.myin.id
}

resource "null_resource" "local2" {
	depends_on = [
    aws_volume_attachment.ebs_att,
  ]
	connection {
    type     = "ssh"
    user     = "ec2-user"
    private_key = file("C:/Users/juzer/Desktop/mykey111.pem")
    host     = aws_instance.myin.public_ip
  }
	provisioner "remote-exec" {
    inline = [
      "sudo mkfs.ext4 /dev/xvdf",
      "sudo mount /dev/xvdf /var/www/html",
      "sudo rm -rf /var/www/html/*",
      "sudo git clone https://github.com/juzer-patan/lwcloud_task1.git /var/www/html/"	
    ]
  }


    }
