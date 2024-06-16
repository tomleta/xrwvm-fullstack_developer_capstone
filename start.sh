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
python3 manage.py migrate --run-syncdb
python3 manage.py createsuperuser
cd frontend
npm install
npm run build

# to start up the MongoDB (which holds the Dealerships and Reviews models)
# docker build . -t nodeapp
# docker-compose up
# launch application on port 3030 and copy that url to .env

# to start up sentiment analyzer microservice
# run in code engine CLI
# docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
# docker push us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
# ibmcloud ce application create --name sentianalyzer --image us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer --registry-secret icr-secret --port 5000
# then need to change URL in server/djangoapp/.env