class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= len(nums)
        start = 0
        count = 0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                next_idx = (current + k) % n
                tmp = prev
                prev = nums[next_idx]
                nums[next_idx] = tmp
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1


s = Solution()
l1 = [1, 2, 3, 4, 5, 6, 7]
s.rotate(l1, 3)
print(l1)
l2 = [-1, -100, 3, 99]
s.rotate(l2, 2)
print(l2)
l3 = [1, 2, 3, 4, 5, 6, 7, 8]
s.rotate(l3, 2)
print(l3)
