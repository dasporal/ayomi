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


from typing import List

def rpn(operations: List[str]) -> float:
    stack = []
    
    for op in operations:
        # Check if the current element is a number or float
        if op.replace('.', '', 1).isdigit():
            stack.append(float(op))
        else:
            if len(stack) < 2:
                raise ValueError("Invalid expression: not enough operands for the operation.")
            
            b = stack.pop()
            a = stack.pop()

            if op == '+':
                stack.append(a + b)
            elif op == '-':
                stack.append(a - b)
            elif op == '*':
                stack.append(a * b)
            elif op == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                stack.append(a / b)
            else:
                raise ValueError(f"Unsupported operator: {op}")
    
    if len(stack) != 1:
        raise ValueError("Invalid expression: too many or too few operators.")
    
    return stack.pop()


@app.post("/calculate")
def calculate_rpn(operations: List[str]):
    try:
        result = rpn(operations)
        return {"result": result}
    except ValueError as e:
        return {"error": str(e)}
