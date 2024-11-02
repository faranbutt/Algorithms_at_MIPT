class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(None,None)
        self.tail = self.head
        self.len = 0

    def insert(self,previous_node,val):
        new_node = Node(val,previous_node.next)
        previous_node.next = new_node
        self.len += 1
        if new_node.next is None:
            self.tail = new_node
        return new_node
    def push_front(self,val):
        return self.insert(self.head,val)
    def push_back(self,val):
        return self.insert(self.tail,val)

    def remove(self,node):
        prev_node = self.head
        while prev_node is not None and prev_node.next != node:
            prev_node = prev_node.next
        if prev_node is not None:
            prev_node.next = node.next
            self.len -= 1
            if prev_node.next is None:
                self.tail = prev_node
            return node.val
        else:
            raise ValueError("node provided not found in the list")

    def remove_front(self):
        return self.remove(self.head.next)
    def remove_tail(self):
        return self.remove(self.tail)
    def __len__(self):
        return self.len
    def __str__(self):
        values = []
        current_node = self.head.next
        while current_node:
            values.append(str(current_node.val))
            current_node = current_node.next
        return '->'.join(values) if values else "Empty List"

x = LinkedList()
x.push_back(1)
print(x)
x.push_front(2)
print(x)