#!/bin/bash

export FLASK_APP=wgsi.py
export APP_CONFIG_FILE=config.py
export FLASK_ENV=development
flask run --port 8880