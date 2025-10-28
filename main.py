import uvicorn
from src.loader import config

if __name__ == "__main__":
    print(f"launching to port={config.port}")
    uvicorn.run("src.app:app", host="0.0.0.0", port=config.port)
