class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.size = 0
        self.k = k
        self.head = self.tail = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.isEmpty():
            self.head -= 1
            self.head += self.k
            self.head %= self.k
        self.size += 1
        self.q[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.isEmpty():
            self.tail += 1
            self.tail %= self.k
        self.size += 1
        self.q[self.tail] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.head += 1
        self.head %= self.k
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.tail -= 1
        self.tail += self.k
        self.tail %= self.k
        return True        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.k


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