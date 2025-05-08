class StockPrice:

    def __init__(self):
        self.mp = defaultdict(int)
        self.s = SortedList()
        self.cur = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp not in self.mp:
            self.s.add(price)
            self.mp[timestamp] = price
        else:
            prev = self.mp[timestamp]
            self.s.discard(prev)
            self.s.add(price)
            self.mp[timestamp] = price
        self.cur = max(self.cur, timestamp)
        # print(self.mp, self.s, self.cur)

    def current(self) -> int:
        return self.mp[self.cur]

    def maximum(self) -> int:
        # print(self.s[-1])
        return self.s[-1]

    def minimum(self) -> int:
        return self.s[0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()