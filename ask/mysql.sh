sudo /etc/init.d/mysql start
mysql -u root -e "create database stepik;"
mysql -u root -e "create user 'django'@'localhost' identified by 'mysite746';"
mysql -u root -e "grant all privileges on stepik.* to 'django'@'localhost' with grant option;"
mysql -u root -e "flush priveleges;"
