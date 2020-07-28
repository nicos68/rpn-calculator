class Operator(object):
    def __init__(self, cardinality=2):
        self._cardinality = cardinality


class AddOperator(Operator):
    def execute(self, left_operand, right_operand):
        return left_operand.execute() + right_operand.execute()


class Value(Operator):
    def __init__(self, value):
        super().__init__(cardinality=0)
        self._value = value

    def execute(self):
        return self._value

class Calculator(object):
    def __init__(self):
        self._stack = []
        self._operator_registry = {
            '+': AddOperator()
        }

    def push(self, value):
        try:
            float(value)
            self._stack.append(Value(value))
        except ValueError:
            if value in self._operator_registry:
                self._stack.append(self._operator_registry[value])

    def execute(self):
        operator = self._stack.pop()
        left_operand = self._stack.pop()
        right_operand = self._stack.pop()
        result = operator.execute(left_operand, right_operand)
        self._stack.append(result)
        return result
