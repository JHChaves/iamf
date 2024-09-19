from http import HTTPStatus

from fastapi import FastAPI

from iamf.routers import auth, todos, users
from iamf.schemas import Message

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Meu belíssimo mundo!!!'}
