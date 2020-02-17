# Welcome to tweet-tracker 👋

![Version](https://img.shields.io/badge/version-0.2-blue.svg?cacheSeconds=2592000)
[![Coverage Status](https://coveralls.io/repos/github/igoreineck/tweet-tracker/badge.svg?branch=master)](https://coveralls.io/github/igoreineck/tweet-tracker?branch=master)
[![Twitter: irseineck](https://img.shields.io/twitter/follow/irseineck.svg?style=social)](https://twitter.com/irseineck)

> A simple application used to track tweets based on inputs given by user

## Settings

To run this application, make sure that you already have Redis installed on your system.
If you don't, try to check for more informations at this link: [(Redis Docs)](https://redis.io/documentation)

Redis connect on port 6379 by default. Make sure that you have this port open.
If you are using some Linux distro, you can check opened ports putting in your terminal this command:

> sudo lsof -i -P -n | grep LISTEN

## Installation

After download this repository you must to install dependencies. Don't forget to create your virtual environment and tap:

> pip install -r requirements.txt

To allow the application communicate with Twitter, you will need to define your API credentials.
You can get more information at: [(Twitter Docs)](https://developer.twitter.com/)

Create a file called ".env" and save into root folder and generate your API_KEY, API_KEY_SECRET, ACCESS_TOKEN and ACCESS_TOKEN_SECRET from Twitter API and save them into this file.

Don't forget to save Redis information into the .env too. The variables are: REDIS_HOST, REDIS_PORT and REDIS_DB

After all, try to run "flask run". And everything should works.

## Author

👤 **Igor Eineck**

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
