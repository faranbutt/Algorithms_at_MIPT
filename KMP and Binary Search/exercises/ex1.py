class Heap():

    def __init__(self):
        self.data = []

    def pop(self):

        res = self.data[0]
        if len(self.data) == 1:
            self.data = []
            return res

        value = self.data[-1]
        pos = 0
        self.data[pos] = value
        self.data.pop(-1)

        if len(self.data) == 1:
            return res
        elif len(self.data) == 2:
            if self.data[1] > self.data[0]:
                self.data[0], self.data[1] = self.data[1], self.data[0]
            return res

        left_child_pos = 1
        left_child = self.data[left_child_pos]
        right_child_pos = 2
        right_child = self.data[right_child_pos]
        while value < left_child or value < right_child:

            if left_child < right_child:
                max_child = right_child
                max_child_pos = right_child_pos
            else:
                max_child = left_child
                max_child_pos = left_child_pos
           
            self.data[pos], self.data[max_child_pos] = self.data[max_child_pos], self.data[pos]
            pos = max_child_pos

            left_child_pos = (2 * pos) + 1
            right_child_pos = (2 * pos) + 2

            if left_child_pos >= len(self.data):
                left_child = (-1, 0)
            else:
                left_child = self.data[left_child_pos]

            if right_child_pos >= len(self.data):
                right_child = (-1, 0)
            else:
                right_child = self.data[right_child_pos]

        return res

    def push(self, value):
        self.data.append(value)
        pos = len(self.data) - 1
        parent_pos =  (pos-1) // 2 
        parent = self.data[parent_pos]
        while value > parent and pos != 0:
            self.data[pos], self.data[parent_pos] = self.data[parent_pos], self.data[pos]
            pos = parent_pos
            parent_pos = (pos-1) // 2
            parent = self.data[parent_pos]

   


n = int(input())

if n != 0:
    first_command = input().split()
    ind = int(first_command[1])
    val = int(first_command[2])
    heap = Heap()
    heap.push((val, -ind))


for i in range(1, n):
    command = input().split()
    if command[0] == '+':
        ind = int(command[1])
        val = int(command[2])
        heap.push((val, -ind))

    elif command[0] == '-':
        res = heap.pop()
        print(-res[1])


    