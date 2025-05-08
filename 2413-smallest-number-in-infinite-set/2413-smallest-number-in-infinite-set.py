class SmallestInfiniteSet:

    def __init__(self):
        self.currentNum = 1
        self.s = SortedSet()

    def popSmallest(self) -> int:
        if self.s:
            smallest = self.s[0]
            self.s.remove(self.s[0])
        else:
            smallest = self.currentNum
            self.currentNum += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.currentNum:
            self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)