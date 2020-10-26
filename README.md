# Coding Challenge App

A skeleton flask app to use for a coding challenge.

## Install:

You can use a virtual environment (conda, venv, etc):
```
conda env create -f environment.yml
source activate user-profiles
```

After your venv is activated, just pip install from the requirements file
``` 
pip install -r requirements.txt
```

## Running the code


### Spin up the service

```
# start up local server
python -m run 
```

### Making Requests

```
curl -i "http://127.0.0.1:5000/profile/<username>"
```

```
curl -i "http://127.0.0.1:5000/health-check"
```

### Running Tests

```
python -m unittest 
```

## What'd I'd like to improve on...

I would like more extensive test coverage via a larger set of fixtures (ideally formatted for PEP8 standards) which cover all edge cases. For example, when a repo does not list a language.  I would also like to mock `requests` and write test cases for HTTP status code of 404.

Mocking the result of `ProfileData.fetch_profile_data` and writing an implementation test in `test_routes.py` wouldn't also be a bad idea.