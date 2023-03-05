import math


class Solution:
    def get_max_len(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        start = 0
        negatives = 0
        max_length = 0
        curr_length = 0
        fst_neg = math.inf
        lst_neg = -math.inf

        for i in range(n + 1):
            if i == n or nums[i] == 0:  # check last interval or finish current one
                if negatives % 2 == 0:
                    max_length = max(max_length, curr_length)  # We can choose whole interval
                else:
                    max_length = max(max_length, max(i - fst_neg - 1, lst_neg - start))  # Remove first or last negative
                start = i + 1  # Start of next interval
                negatives = 0
                curr_length = 0
                fst_neg = math.inf
                lst_neg = -math.inf
                continue
            elif nums[i] < 0:
                negatives += 1
                fst_neg = min(fst_neg, i)
                lst_neg = max(lst_neg, i)
            curr_length += 1
        return max_length


s = Solution()
print(s.get_max_len([1, -2, -3, 4]))
print(s.get_max_len([0, 1, -2, -3, -4]))
print(s.get_max_len([-1, -2, -3, 0, 1]))
print(s.get_max_len([-1, 2]))
