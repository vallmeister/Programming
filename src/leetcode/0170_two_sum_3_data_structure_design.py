class TwoSum:

    def __init__(self):
        self.nums = set()
        self.sums = set()

    def add(self, number: int) -> None:
        for num in self.nums:
            self.sums.add(num + number)
        self.nums.add(number)

    def find(self, value: int) -> bool:
        return value in self.sums
