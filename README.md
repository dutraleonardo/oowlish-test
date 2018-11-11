# Github users api.

## Main tools used in this project

* Ubuntu 16.04 LTS
* Visual Studio Code
* Python 3.5.2
* Django 2.1.3
* Django REST Framework 3.9.0


## Getting Started

### Prerequisites

* Python 3.5.2


### Installing

1. Create a virtual environment:

```
$ virtualenv <env_name>
$ source <env_name>/bin/activate
```

2. Mount enviroment(Install dependencies and apply migrations):

```
$ make dev_enviroment # to dev enviroment
```
or 
```
$ make prod_enviroment # to production env
```

3. Start the server:

```
$ make run
```

The site will be available on <http://0.0.0.0:8000>.


## REST API

REST API docs can be found in <http://0.0.0.0:8000/api/v1/docs/>

## Authors

* **José Leonardo De Dutra** 
