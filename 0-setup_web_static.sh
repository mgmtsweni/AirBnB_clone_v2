#!/usr/bin/env bash
## Sets up a web server for deployment of web_static.

sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo ufw allow 'Nginx HTTP'
echo -e "\e[1;32m Packages updated\e[0m"

sudo mkdir -p /data/web_static/releases/test
echo "This is the School" > /data/web_static/releases/test/index.html
sudo mkdir /data/web_static/shared/
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
