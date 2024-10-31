class Queue:
    def __init__(self):
        self._queue = []
        self.length = 0

    def push(self,value):
        self._queue.append(self.length)
        self.length += 1
    def pop(self):
        dummy = self._queue[0]
        del (self._queue[0])
        self.length -= 1
        return dummy
    def front(self):
        return self._queue[0]
    def print(self):
        print(self._queue)
    def len(self):
        print("Length of queue = ",self.length)
q = Queue()
q.len()
q.push(0)
q.push(1)
q.push(2)
q.print()
q.len()
print(q.pop())
print(q.pop())
print(q.pop())
q.print()
q.len()