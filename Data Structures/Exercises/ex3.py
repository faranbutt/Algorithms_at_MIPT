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

    def insert_at(self, index, data):
        if index < 0 or index > self.len:
            print("Error! Index out of bounds.")
            return
        new_node = Node(data)
        if index == 0:
            self.push_front(data)
        elif index == self.len:
            self.push_back(data)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            new_node.previous = current
            current.next.previous = new_node
            current.next = new_node
            self.len += 1

    def length(self):
        return self.len

if __name__=="__main__":
    num_stores = int(input())
    ll = DoubleLL()
    while True:
        a = tuple(input().split())
        if a[0] == "+":
            ll.push_back(a[2])
        elif a[0] == "?":
            print(ll.length())
        elif a[0] == "-":
            cc = ll.pop_front()
            print(cc)
        elif a[0] == "#":
            break



