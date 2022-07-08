import os
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum

STAGE = os.environ.get('STAGE', None)
openapi_prefix = "/" if not STAGE else f'/{STAGE}'

app = FastAPI(title="MyAwesomeApp", root_path=openapi_prefix)

# Mangum Handler, this is so important
handler = Mangum(app)


@app.get("/")
def index():
    return {"message": "up"}


class User(BaseModel):
    id: int
    email: str
    password: str


users_list = [
    User(id=1, email="developer@hp.com", password="******"),
    User(id=2, email="sysops@hp.com", password="******")
]


@app.get("/users")
def get_users():
    return users_list


@app.get("/users/{id}")
def get_user_by_id(id: int):
    for user in users_list:
        if (user.id == id):
            return user
    # TODO: change response status code
    return {"status": 404}


@app.post("/user")
def create_user(user: User):
    # TODO validate request before append
    users_list.append(user)
    return user

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
