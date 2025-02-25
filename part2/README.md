# Part 2 HBnB - BL and API

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This project is to simulate actual working AirBnB website.
This to demostrate the implementation of Business Logic and API Endpoints


The project directory structure is 


```hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```
**Explanation:**

     The `app/` directory contains the core application code.
     The `api/` subdirectory houses the API endpoints, organized by version (`v1/`).
     The `models/` subdirectory contains the business logic classes (e.g., `user.py`, `place.py`).
     The `services/` subdirectory is where the Facade pattern is implemented, managing the interaction between layers.
     The `persistence/` subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQL Alchemy.
     `run.py` is the entry point for running the Flask application.
     `config.py` will be used for configuring environment variables and application settings.
     `requirements.txt` will list all the Python packages needed for the project.
     `README.md` will contain a brief overview of the project.

## Getting Started <a name = "getting_started"></a>



These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.


### Prerequisites

What things you need to install the software and how to install them.



**Install Required Packages**

   Python packages are as below and listed in requirements.txt 

```bash
    flask
    flask-restx
```
### Installing

It is recommended to install and run packages in the virtual environment so that correct packages/library versions are consistently used every time the software runs

Please refer to https://phoenixnap.com/kb/install-flask for detailed information on installing virtualenv module and activating the virtual enviroment.
   
Install the dependencies using:

```bash
    pip install -r requirements.txt
```


## Usage <a name = "usage"></a>

```bash
    python3 run.py
```

The server should be running with the output below

```bash
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 540-870-112
 ```
