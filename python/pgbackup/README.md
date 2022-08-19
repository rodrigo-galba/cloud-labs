pgbackup
========

CLI for backing up remote PostgreSQL databases locally or to AWS S3.

## Usage

Local Example w/ local path:

```
$ pgbackup postgres://bob@example.com:5432/db_one
```

## Installation From Source

```
pip install --user -e .
```

## Preparing for Development

Follow these steps to start developing with this project

1. Ensure `pip`and `pipenv` are installed
2. Clone respository
3. `cd`into repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`

## Docker setup

TBD

## Gitignore

```
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore
```