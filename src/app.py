from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.exceptions.code_exception import CodeException
from src.handlers import news, schedule

app = FastAPI()
app.include_router(news.router)
app.include_router(schedule.router)


@app.exception_handler(CodeException)
async def unicorn_exception_handler(request: Request, exc: CodeException):
    return JSONResponse(
        status_code=exc.error_code,
        content=exc.message,
    )
