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

    def insert_middle(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            mid = self.len // 2
            if mid < self.len // 2:
                current = self.head
                for _ in range(mid):
                    current = current.next
            else:
                current = self.tail
                for _ in range(self.len - mid - 1):
                    current = current.previous

            if self.len % 2 == 0:
                new_node.next = current
                new_node.previous = current.previous

                if current.previous:
                    current.previous.next = new_node
                current.previous = new_node

                if mid == 0:
                    self.head = new_node
                else:
                    new_node.previous.next = new_node
            else:
                new_node.previous = current
                new_node.next = current.next

                if current.next:
                    current.next.previous = new_node
                current.next = new_node

                if current == self.tail:
                    self.tail = new_node

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
            results.append(customer)

        elif command[0] == "?":
            store_id = int(command[1])
            results.append(queues[store_id].length())

        elif command[0] == "#":
            break

    for result in results:
        print(result)
