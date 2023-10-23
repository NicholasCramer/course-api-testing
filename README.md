# course-api-testing
 Learning API testing with Pytest - Udemy Course: https://www.udemy.com/course/backend-api-testing-with-python

## Set up instructions

### Step 1:
Install virtual environment

Virtual environment setup notes:
```
Step 1:
pip install virtualenv

Step 2:
In project folder (C:\Users\nick_\Projects\course-api-testing)
python -m virtualenv venv_pyapi_py3
(creates the virtualenv with specified name)

Step 3: Activate virtualenv
venv_pyapi_py3\Scripts\activate.bat

Step 4: Do pip installs for desired projects

pip install requests
pip install pytest
pip install pymysql

pip freeze (outputs installed packages in order of requirements)

```

### Step 2: 
Install setup.py file

```
python setup.py install

python setup.py develop (any time a change is made to any packages, it will work right away)
	
```

### Step 3:
Create wordpress site and mysql database Docker containers

```
cd Projects\course-api-testing\wordpress_site\wordpress

docker compose up -d (runs docker-compose.yml file) creates new containers

To end docker container, docker compose stop
To start container, docker compose start

To delete, docker compose down
```

### Step 4:
With Docker containers running, do any required setup on the local instance of the wordpress site.
Setup API keys and import as environment variables

```
Setting environment variables such as credentials:
	SET WC_KEY='Value'
	SET WC_SECRET='Value'
```

## Pytest - running tests

All Python code is in the apitest directory
`cd apitest/tests`

You can run all tests with the command `pytest`

You can run groups of tests by the it's marker: 'regression', 'smoke', 'products' etc: `pytest -m smoke`

You can run individual test cases by their marker as well: `pytest -m tcid40`

To generate html test reports using the pytest-html plugin:
```
pytest --html=report.html --self-contained-html
```



