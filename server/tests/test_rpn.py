from app.rpn_calculator import rpn
import pytest

def test_rpn_calculator_valid():
    assert rpn(["3", "4", "+", "2", "*"]) == 14
    assert rpn(["5", "1", "2", "+", "4", "*", "+", "3", "-"]) == 14

def test_rpn_calculator_invalid_too_many_operators():
    with pytest.raises(ValueError, match="not enough operands for the operation"):
        rpn(["3", "4", "2", "*", "+", "*"])

def test_rpn_calculator_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        rpn(["10", "0", "/"])

def test_rpn_calculator_unrecognized_operator():
    with pytest.raises(ValueError, match="Unsupported operator"):
        rpn(["3", "4", "%"])

def test_rpn_calculator_invalid_final_stack():
    with pytest.raises(ValueError, match="Invalid expression: too many or too few operators."):
        rpn(["3", "4", "2", "*"])
