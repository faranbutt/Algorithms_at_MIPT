class Vector:
    def make(self,x):
        self.arr = [0] * x
        self.capacity  = x
    def push(self,value):
        print((len(self.arr)-1)-(self.capacity-1))
        self.arr[(len(self.arr)-1)-(self.capacity-1)] = value
        self.capacity -= 1
    def get(self,i):
        return self.arr[i]
    def set(self,i,value):
        self.arr[i] = value
    def print(self):
        return self.arr

vec  = Vector()
vec.make(10)
print(vec.print())
vec.push(2)
print(vec.print())
vec.push(22)
print(vec.print())
vec.push(33)
print(vec.print())