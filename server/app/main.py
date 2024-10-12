from fastapi import FastAPI
from .database import engine
from .models import Base
from .api import routes
import uvicorn
import socket

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routes.router)

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0)) 
        return s.getsockname()[1]

if __name__ == "__main__":
    port = find_free_port()
    print(f"Starting server on port {port}")
    uvicorn.run("app.main:app", host="127.0.0.1", port=port, reload=True)
