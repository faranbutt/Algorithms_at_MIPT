class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoubleLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def is_empty(self):
        return self.head is None

    def push_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.len += 1

    def push_back(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.len += 1
    def pop_front(self):
        if self.is_empty():
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        self.len -= 1
        return data

    def pop_back(self):
        if self.is_empty():
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        self.len -= 1
        return data
    def length(self):
        return self.len

if __name__=="__main__":
    inp = 0
    t = []
    ll = DoubleLL()
    while True:
        a = tuple(map(int,input().split()))
        if a[0] == 0:
            ll.push_back(a[1])

        elif a[0] == 1:
            ll.push_front(a[1])

        elif a[0] == 2:
            print(ll.length())

        elif a[0] == 3:
            cc = ll.pop_back()
            if cc == None:
                print("Error!")
            else:
                print(cc)

        elif a[0] == 4:
            bb = ll.pop_front()
            if bb == None:
                print("Error!")
            else:
                print(bb)
        elif a[0] == -1:
            break




