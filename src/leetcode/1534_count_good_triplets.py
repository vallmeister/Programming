from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        ans += 1
        return ans


s = Solution()
print(s.countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3))
print(s.countGoodTriplets(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1))
print(s.countGoodTriplets([7, 3, 7, 3, 12, 1, 12, 2, 3], 5, 8, 1))
