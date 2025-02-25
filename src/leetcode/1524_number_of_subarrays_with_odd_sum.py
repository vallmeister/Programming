from typing import List


# try again with more intuitive calculation
class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        ps = [0] * n
        ps[0] = arr[0]
        for i in range(1, n):
            ps[i] = ps[i - 1] + arr[i]
        even = [0] * (n + 1)
        odd = [0] * (n + 1)
        for i in reversed(range(n)):
            if ps[i] % 2 == 0:
                even[i] = even[i + 1] + 1
                odd[i] = odd[i + 1]
            else:
                odd[i] = odd[i + 1] + 1
                even[i] = even[i + 1]
        ans = 0
        for i in range(n):
            if ps[i] % 2 == 0:
                ans += odd[i]
            else:
                ans += even[i] + 1
            ans %= MOD
        return ans


s = Solution()
print(s.numOfSubarrays([1, 3, 5]))
print(s.numOfSubarrays([2, 4, 6]))
print(s.numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))
