#!/usr/bin/env bash

virtualenv venv --python=python3
curl https://bootstrap.pypa.io/get-pip.py | venv/bin/python
venv/bin/pip install -r requirements/base.txt
venv/bin/python ./manage.py migrate

npm install
npm install gulp -g
npm install gulp-cli -g

venv/bin/python ./manage.py runserver