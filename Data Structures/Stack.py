class Stack:
    def __init__(self):
        self._stack = []

    def push(self,value):
        self._stack.append(value)
    def isEmpty(self):
        return not self._stack
    def print(self):
        print(self._stack)
    def pop(self):
        if self.isEmpty():
            return None
        return self._stack.pop()


a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.print()
print(a.pop())
a.print()



