from fastapi import FastAPI
from typing import List
import uvicorn
import socket

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Ayomi"}

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0)) 
        return s.getsockname()[1]

if __name__ == "__main__":
    port = find_free_port()
    print(f"Starting server on port {port}")
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)

