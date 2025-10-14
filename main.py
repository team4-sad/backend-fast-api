import uvicorn
from src.loader import config

uvicorn.run("src.app:app", host="0.0.0.0", port=config.PORT)
