class StockSpanner:

    def __init__(self):
        self.ms = []

    def next(self, price: int) -> int:
        ans = 1
        while self.ms and price >= self.ms[-1][0]:
            _, days = self.ms.pop()
            ans += days
        self.ms.append((price, ans))
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
