[![Build Status](https://travis-ci.com/MagzKr/askwer.svg?branch=master)](https://travis-ci.com/MagzKr/askwer)
# Askwer
This is a project in which i made a simple clone of Stack Owerflow using Django.

## Application link
[Askwer](https://askwer-app.herokuapp.com/)

## Features
- Django 3.1
- PostgreSQL
- Dockerized using Docker-Compose
- Test and build using Travis CI
- Deploy on Heroku

## How to run

```bash
#download project
$ git clone https://github.com/MagzKr/askwer

# create python virtual environment
$ python3 -m venv myenv
$ source myenv/bin/activate

# install requirements
$ pip install -r requirements.txt

#set environment variables
$ source .env

#build and run app in docker
$ docker-compose build
$ docker-compose up

#run app using db in docker
$ docker compose up -d db
$ bash entrypoint.sh
```


