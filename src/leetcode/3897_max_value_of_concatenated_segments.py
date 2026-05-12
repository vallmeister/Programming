class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        MOD = 10 ** 9 + 7
        segments = list(zip(nums1, nums0))
        pure_ones = sum(ones for ones, zeroes in segments if zeroes == 0)
        ans = 0
        for _ in range(pure_ones):
            ans *= 2
            ans += 1
            ans %= MOD
        for ones, zeroes in sorted(filter(lambda t: t[1] > 0, segments), key=lambda t: (-t[0], t[1])):
            for _ in range(ones):
                ans *= 2
                ans += 1
                ans %= MOD
            for _ in range(zeroes):
                ans *= 2
                ans %= MOD
        return ans


s = Solution()
print(s.maxValue(nums1=[1, 2], nums0=[1, 0]))
print(s.maxValue(nums1=[3, 1], nums0=[0, 3]))
