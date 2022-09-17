# Sleepers - HackZurich 2022 Challenge #9 - Backend (FastAPI)
## Development enviroment
### Requirements
Python 3.7+

FastAPI stands on the shoulders of giants:
- Starlette (https://www.starlette.io/) for the web parts.
- Pydantic (https://pydantic-docs.helpmanual.io/) for the data parts.

### Installation
Create new python env
```
$ python3 -m venv hackzurich-env
```
Activate new env
```
$ source hackzurich-env/bin/activate
```
Install FastAPI
```
$ (hackzurich-env) python -m pip install -r requirements.txt
```

## Run API
```
uvicorn main:app --reload
```
### Interactive API docs
Now go to http://127.0.0.1:8000/docs
You will see the automatic interactive API documentation (provided by Swagger UI)

### Alternative API docs
And now, go to http://127.0.0.1:8000/redoc
You will see the alternative automatic documentation (provided by ReDoc)