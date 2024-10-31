from os import remove


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


    def push_back(self,val):
        return self.insert(self.tail,val)
    def push_front(self,val):
        return self.insert(self.head,val)

    def print_ll(self):
        curr = self.head.next
        arr = []
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        print('->'.join(map(str,arr)))

    def remove(self,node):
        previous_node = self.head
        while previous_node.next is not None and previous_node.next != node:
            previous_node = previous_node.next
        if previous_node.next is not None:
            previous_node.next = node.next
            self.len -= 1
            if node.next is None:
                self.tail = previous_node
    def pop_front(self):
        if self.head is not None:
            self.remove(self.head.next)
    def pop_back(self):
        if self.head is not None:
            current = self.head
            while current.next and current.next.next:
                current = current.next
            self.remove(current.next)
    def length(self):
        return self.len







ll  = LinkedList()
ll.push_back(1)
ll.push_back(2)
ll.push_front(3)

ll.print_ll()

ll.pop_front()
ll.print_ll()
ll.push_front(23)
ll.push_front(2)
ll.print_ll()
ll.pop_back()
ll.print_ll()
