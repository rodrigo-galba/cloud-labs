## fastapi

```
mkdir FastAPI-Lambda-Function
cd FastAPI-Lambda-Function
python3 -m venv venv
source venv/bin/activate
pip install fastapi mangum uvicorn
pip freeze > requirements.txt
npm i -g serverless
```

### Create Lambda execution role

```
aws iam create-role --role-name lambda-execution-role --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
```

#### Serverless setup

On windows:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

On WSL 2 #use NVM

```

```

## pipenv

On windows
```
C:\Users\user\AppData\Roaming\Python\Python310\Scripts\pipenv.exe --python python
C:\Users\user\AppData\Roaming\Python\Python310\Scripts\pipenv.exe shell
```

## CLI app

- Database backup tool
- EC2 instance backup tool

## Upgrade to Python 3.10

Ubuntu:

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
apt list | grep python3.10
sudo apt install python3.10
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2
sudo update-alternatives --config python3
sudo apt remove --purge python3-apt
sudo apt autoclean
sudo apt install python3-apt
sudo apt install python3.10-distutils
sudo apt install python3.10-venv
python3 -m venv venv
source venv/bin/activate
pip install pipenv
pipenv shell
```

## Running Postgresl

```
docker-compose up
```

### Install postgresl client

Go to WSL:
```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt -y update
sudo apt install postgresql-client-14
```

Connect to DB:
```
pg_dump -h 192.168.50.130 -U userdb -d userdb # userdb
```

### Git ignore

```
wget https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore -O .gitignore
```

References

- https://adem.sh/blog/tutorial-fastapi-aws-lambda-serverless
- https://fastapi.tiangolo.com/
- https://dwisulfahnur.medium.com/fastapi-deployment-to-aws-lambda-with-serverless-framework-b637b455142c
- https://docs.microsoft.com/pt-br/windows/dev-environment/javascript/nodejs-on-wsl
- https://www.pythontutorial.net/python-basics/install-pipenv-windows/
- https://cloudbytes.dev/snippets/upgrade-python-to-latest-version-on-ubuntu-linux
