class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return str(self.find_kth_bit_helper(n, k))

    def find_kth_bit_helper(self, n, k):
        if k == 1:
            return 0
        length = 2 ** n - 1
        if k == length // 2 + 1:
            return 1
        elif k <= length // 2:
            return self.find_kth_bit_helper(n - 1, k)
        else:
            return 1 - self.find_kth_bit_helper(n - 1, length - k + 1)
