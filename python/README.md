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

References

- https://adem.sh/blog/tutorial-fastapi-aws-lambda-serverless
- https://fastapi.tiangolo.com/
- https://dwisulfahnur.medium.com/fastapi-deployment-to-aws-lambda-with-serverless-framework-b637b455142c
- https://docs.microsoft.com/pt-br/windows/dev-environment/javascript/nodejs-on-wsl
- https://www.pythontutorial.net/python-basics/install-pipenv-windows/