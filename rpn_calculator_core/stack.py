class Stack(object):
    def __init__(self):
        self._stack = []

    def push(self, value):
        self._stack.append(value)