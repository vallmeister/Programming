class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prefix_product = [1]
        self.last_zero = -1

    def add(self, num: int) -> None:
        n = len(self.nums)
        self.nums.append(num)
        prev = self.prefix_product[-1]
        if num == 0:
            self.last_zero = n
            self.prefix_product.append(prev)
        else:
            self.prefix_product.append(prev * num)

    def getProduct(self, k: int) -> int:
        n = len(self.nums)
        if n - k <= self.last_zero:
            return 0
        else:
            return self.prefix_product[-1] // self.prefix_product[-k - 1]

# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
