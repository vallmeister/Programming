from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        stack =[]

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                count = (mid - left) * (right - mid)
                ans += count * arr[mid]
                ans %= MOD
            stack.append(i)
        return ans


s = Solution()
print(s.sumSubarrayMins([3, 1, 2, 4]))
print(s.sumSubarrayMins([11, 81, 94, 43, 3]))
