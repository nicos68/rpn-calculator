from rpn_calculator_core.rpn_calculator import Calculator, AddOperator, Value
import pytest


@pytest.fixture
def simple_calculator():
    calculator = Calculator()
    calculator.push(1)
    calculator.push(2)
    return calculator


def test_push(simple_calculator):
    assert simple_calculator._stack[0].execute() == 1
    assert simple_calculator._stack[1].execute() == 2


def test_operator():
    operator = AddOperator()
    assert operator.execute(Value(1), Value(2)) == 3


def test_execute(simple_calculator):
    simple_calculator.push('+')
    assert simple_calculator.execute() == 3
    assert simple_calculator._stack[0].execute() == 3


