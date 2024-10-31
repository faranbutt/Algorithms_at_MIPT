class Vector:
    def make(self,x):
        self.arr = [None] * x
        self.capacity  = x
    def push(self,value):
        self.arr[(len(self.arr)-1)-(self.capacity-1)] = value
        self.capacity -= 1
    def len(self):
        l = 0
        for i in self.arr:
            if i != None:
                l += 1
        return l
    def get(self,i):
        return self.arr[i]
    def set(self,i,value):
        for k in range(i,self.len()):
            self.arr[k+1] = self.arr[k]
        self.arr[i] = value
        return
    def print(self):
        return self.arr

vec  = Vector()
vec.make(10)
vec.push(1)
vec.push(2)
vec.push(3)
vec.set(1,3)
vec.set(3,100)
print(vec.print())
