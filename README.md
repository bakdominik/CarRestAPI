
# Cars REST API

Basic car makes and model database interacting with an external [API](https://vpic.nhtsa.dot.gov/api/).

## Demo

Here is a working live demo : [https://carsrestapi.herokuapp.com/](https://iharsh234.github.io/WebApp/).

## Features
- Add car if its make and model are present in [NHTSA VIPIC API](https://vpic.nhtsa.dot.gov/api/)
- Delete car
- Rate car
- Display cars
- Display top cars ranking based on a number of rates
## Setup
### Using Docker
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/bakdominik/CarRestAPI
$ cd CarRestApi
```
Pull image from the DockerHub repository:
```sh
$ docker pull -all-tags bakdominik/carsrestapi
```
Run App:
```sh
$ docker run -d --name carsrestapi -e "PORT=8765" -e "DEBUG=1" -p 8000:8765 bakdominik/carsrestapi:latest
```
And navigate to `http://localhost:8000/` to see a list of possible endpoints.

### Using Virtual Environment
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/bakdominik/CarRestAPI
$ cd CarRestApi
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv ./venv
$ . venv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/` to see a list of possible endpoints.

## Technologies

- [Python3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Heroku](https://www.heroku.com/home)
- [NHTSA VIPIC API](https://vpic.nhtsa.dot.gov/api/)

