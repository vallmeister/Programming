class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        start = count = 0
        while count < n:
            curr_idx = start
            prev_element = nums[curr_idx]
            while True:
                curr_idx = (curr_idx + k) % n
                nums[curr_idx], prev_element = prev_element, nums[curr_idx]
                count += 1
                if start == curr_idx:
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
