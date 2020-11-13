#!/bin/bash
export FLASK_APP=app.py
export FLASK_ENV=development
hostname -i
python -m flask run -h $?
