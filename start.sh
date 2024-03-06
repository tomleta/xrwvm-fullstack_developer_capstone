#!/usr/bin/env bash
git config --global user.email "matt@matthewstockinger.com"
git config --global user.name "Matthew Stockinger"
cd server
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate
python3 -m pip install -U -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
cd frontend
npm install
npm run build