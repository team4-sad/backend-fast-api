from fastapi import FastAPI
from src.handlers import test

app = FastAPI()

app.include_router(test.router)
