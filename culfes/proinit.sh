#!/bin/sh

sudo git clone https://github.com/duoshuo/duoshuo-python-sdk.git
cd duoshuo-python-sdk
sudo python setup.py install
cd ..

sudo git clone https://github.com/GeeTeam/gt-python-sdk.git
cd gt-python-sdk
sudo python setup.py install
cd ..

sudo pip install -r requirement.txt
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
