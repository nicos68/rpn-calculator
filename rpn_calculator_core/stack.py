class Operator(object):
    def __init__(self, cardinality=2):
        self._cardinality = cardinality


class AddOperator(Operator):
    def execute(self, left_operand, right_operand):
        return left_operand + right_operand


class Stack(object):
    def __init__(self):
        self._stack = []

    def push(self, value):
        self._stack.append(value)