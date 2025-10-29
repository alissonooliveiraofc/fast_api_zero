from http import HTTPStatus

from fastapi import FastAPI

from fast_api_zero.schemas import Message

app = FastAPI(title="Minha primeira API em Python")


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá Mundo"}
