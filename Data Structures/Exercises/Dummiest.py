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
        self.middle = None  # Track middle node

    def is_empty(self):
        return self.head is None

    def push_back(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = self.middle = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            if self.len % 2 == 0:
                self.middle = self.middle.next
        self.len += 1

    def pop_front(self):
        if self.is_empty():
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = self.middle = None
        else:
            self.head = self.head.next
            self.head.previous = None
            if self.len % 2 == 1:
                self.middle = self.middle.previous
        self.len -= 1
        return data

    def insert_middle(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = self.middle = new_node
        else:
            if self.len % 2 == 1:  # Update middle pointer on odd length
                self.middle = self.middle.next
            new_node.next = self.middle
            new_node.previous = self.middle.previous
            if self.middle.previous:
                self.middle.previous.next = new_node
            self.middle.previous = new_node
            if self.middle == self.head:
                self.head = new_node
            else:
                new_node.previous.next = new_node

        self.len += 1

    def length(self):
        return self.len


if __name__ == "__main__":
    num_stores = int(input().strip())
    queues = [DoubleLL() for _ in range(num_stores)]
    results = []

    while True:
        line = input().strip()
        if not line:
            continue

        command = line.split()

        if command[0] == "+":
            store_id = int(command[1])
            customer_id = int(command[2])
            queues[store_id].push_back(customer_id)

        elif command[0] == "!":
            store_id = int(command[1])
            customer_id = int(command[2])
            queues[store_id].insert_middle(customer_id)

        elif command[0] == "-":
            store_id = int(command[1])
            customer = queues[store_id].pop_front()
            results.append(str(customer))

        elif command[0] == "?":
            store_id = int(command[1])
            results.append(str(queues[store_id].length()))

        elif command[0] == "#":
            break

    print("\n".join(results))