sudo ln /home/box/web/etc/nginx.conf /etc/nginx/conf.d/test.conf
sudo gunicorn -c ~/web/etc/gunicorn.conf hello:application
cd ask
sudo django-admin runserver 0.0.0.0:8000
cd ..
sudo service nginx reload