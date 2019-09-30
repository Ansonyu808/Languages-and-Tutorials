# MySQL

### Installation (For Ubuntu as a local host server)
This is not as easy as it seems if you are configuring MySQL with a password
Followed [this](https://support.rackspace.com/how-to/installing-mysql-server-on-ubuntu/)
* Install MySQL ```sudo apt install mysql-server```
* vLaunch the secure installation utility ```sudo mysql_secure_installation_utility```
* Maybe ufw stuff here if remote access becomes a problem.  I don't think it will.

In order to allow login with a password (For whatever reason, I can never get the password correct at setup) I followed [this](https://superuser.com/questions/603026/mysql-how-to-fix-access-denied-for-user-rootlocalhost) guide from superuser. and [this](https://stackoverflow.com/questions/39281594/error-1698-28000-access-denied-for-user-rootlocalhost) guide from stack overflow.  Steps;
* Login  ```sudo mysql``` 
* Create a new user (Allows you to always sudo mysql and login as root.  Also, it's safer in case you mess up at any stage of changing your password.):
	* ```CREATE USER 'YOUR_SYSTEM_USER'@'localhost' IDENTIFIED BY '';```
	* ```GRANT ALL PRIVILEGES ON *.* TO 'YOUR_SYSTEM_USER'@'localhost';```
	* ```UPDATE user SET plugin='auth_socket' WHERE User='YOUR_SYSTEM_USER';```

* In MySQL CLI update the table with the password:
	* ```update user set authentication_string=password('your_password')where user='test'```
	* ```flush privileges```
* Exit MySQL with <C-d> or exit;
* restart your system if you havent seen the updates take effect:
	* ```service mysql restart```
	* or ```sudo reboot```
