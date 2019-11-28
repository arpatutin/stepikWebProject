sudo /etc/init.d/mysql start
mysql -u root -e "create database stepik;"
mysql -u root -e "create user 'django'@'localhost' identified by 'mysite746';"
mysql -u root -e "grant all privileges on stepik.* to 'django'@'localhost' with grant option;"
./ask/manage.py makemigrations
./ask/manage.py makemigrations qa
./ask/manage.py migrate
sudo ln ~/web/etc/nginx.conf /etc/nginx/conf.d/test.conf
sudo rm -r /etc/nginx/sites-enabled/default
sudo service nginx restart
