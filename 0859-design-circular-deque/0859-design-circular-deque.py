class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.deque = [0]*self.size
        self.head = 0
        self.tail = 0
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.head = (self.head-1+self.size)%self.size
            self.deque[self.head] = value
            self.count += 1
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.deque[self.tail] = value
            self.tail = (self.tail+1)%self.size
            self.count += 1
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.head = (self.head+1)%self.size
            self.count -= 1
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.tail = (self.tail-1+self.size)%self.size
            self.count -= 1
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.deque[(self.tail-1+self.size)%self.size]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == len(self.deque)

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()