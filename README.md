# Init API for this project

`$ make clean`

`$ make migrations`

`$ make migrations-snippets`

`$ make migrate`

`$ make superuser`

`$ make run`

# Migrate command

```
make migrate
```

# migrations command

```
make migrations
```

or (`snippets` is an app for this project)

```
make migrations-snippets
```

## Create superuser

```
make superuser
```

# If you already setup project, run

```
make run
```

## Testing our API (with CURL command-line)

```
~$ curl -u admin -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/users/
```

# if you have migrations in snippets module

## migrations snippets

```
make migrations-snippets
```

`for future update Makefile`

```
make migrations MIGRATION_NAME=snippets
```

## migrate snippets

```
make migrate-snippets
```

```
make migrate MIGRATION_NAME=snippets
```

# Using HTTPIE

Get a list of snippets

```
http http://127.0.0.1:8000/snippets/
```

Get a snippet with `id` = 2

```
http http://127.0.0.1:8000/snippets/2/
```

If we try to create a snippet without authenticating, we'll get an error:

```
http POST http://127.0.0.1:8000/snippets/ code="print(123)"

{
    "detail": "Authentication credentials were not provided."
}
```

We can make a successful request by including the correct username and password:

```
http -a admin:root POST http://127.0.0.1:8000/snippets/ code="print(789)"

{
    "id": 1,
    "owner": "admin",
    "title": "foo",
    "code": "print(789)",
    "linenos": false,
    "language": "python",
    "style": "friendly"
}
```

# Postgres DB

Create DB

```
psql -U postgres
```

```
CREATE DATABASE pastebinapi_db;
```

```
CREATE USER admin WITH PASSWORD 'SXCiKvMy8#4&*W&nNT5kGX&Q2EmUKmx#nu6rDT$djdD4dHfPmnW6JFXx8dqTKhPoVfa7ZZnLmNViC4kp34UpCYg2*@YXEnqB84##fDFxmVG';
```

```
GRANT ALL PRIVILEGES ON DATABASE pastebinapi_db TO admin;
```

# API Documentation

Here the [Swagger Documentation](http://127.0.0.1:8000/api/doc/swagger/)

Here the [Redoc Documentation](http://127.0.0.1:8000/api/doc/redoc/)

# Deployment Essentials to Heroku

Requirements.txt: Create a file listing all your dependencies:

```
pip freeze > requirements.txt
```

Create a Procfile in your project root and add:

```
web: gunicorn PastebinAPI.wsgi --log-file -
```

Runtime.txt (Optional): Specify your Python version:

```
python-3.10.0
```
