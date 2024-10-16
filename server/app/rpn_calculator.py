from typing import List, Union

def rpn(operations: List[Union[float, str]]) -> float:
    stack = []
    for op in operations:
        if isinstance(op, (int, float)):  # Handle both integers and floats directly
            stack.append(op)
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

