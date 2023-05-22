from collections import defaultdict


class FirstUnique:

    # TODO: reimplement with ordered dict
    def __init__(self, nums: list[int]):
        self.counter = defaultdict(int)
        self.num_list = []
        for num in nums:
            self.counter[num] += 1
        for num in nums:
            if self.counter[num] == 1:
                self.num_list.append(num)

    def showFirstUnique(self) -> int:
        return self.num_list[0] if self.num_list else -1

    def add(self, value: int) -> None:
        if self.counter[value] == 0:
            self.counter[value] += 1
            self.num_list.append(value)
        elif value in self.num_list:
            self.num_list.remove(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
