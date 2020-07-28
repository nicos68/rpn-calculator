from rpn_calculator_core.stack import Stack

def test_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack._stack == [1, 2]
