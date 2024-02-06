class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.k = combinationLength
        self.n = len(characters)
        self.bit_mask = (1 << self.n) - (1 << self.n - self.k)

    def next(self) -> str:
        ans = []
        for i in range(self.n):
            if self.bit_mask & (1 << self.n - i - 1):
                ans.append(self.characters[i])
        self.bit_mask -= 1
        while self.bit_mask > 0 and self.bit_mask.bit_count() != self.k:
            self.bit_mask -= 1
        return ''.join(ans)

    def hasNext(self) -> bool:
        return self.bit_mask > 0


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator('abc', 2)
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())

obj = CombinationIterator('chp', 1)
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.hasNext())
print(obj.hasNext())
