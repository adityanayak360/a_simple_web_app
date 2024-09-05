#!/bin/bash
apt update
apt install python3-pip -y
apt install zip
cd /home/ubuntu/
unzip flask-app.zip
cd /home/ubuntu/flask-app
pip install -r requirements.txt