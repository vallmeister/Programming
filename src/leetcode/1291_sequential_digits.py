from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1, 10):
            prev_digit = i
            curr_num = i
            while curr_num <= high:
                if curr_num >= low:
                    ans.append(curr_num)
                prev_digit += 1
                if prev_digit > 9:
                    break
                curr_num *= 10
                curr_num += prev_digit

        return sorted(ans)


s = Solution()
print(s.sequentialDigits(100, 300))
print(s.sequentialDigits(1000, 13000))
