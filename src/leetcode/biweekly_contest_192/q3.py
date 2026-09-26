class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            curr_sum = 0
            pos = [0] * k
            neg = [0] * k
            for j in range(i, n):
                num = nums[j]
                curr_sum += num
                if num > 0:
                    pos[num % k] += 1
                elif num < 0:
                    neg[num % k] += 1
                    pos[num % k] += 1
                r = curr_sum % k
                negate_pos = r % 2 == 0 and pos[r // 2] > 0 or (r + k) % 2 == 0 and pos[(r + k) // 2] > 0
                if r == 0 or negate_pos:
                    ans = max(ans, j - i + 1)
        return ans


s = Solution()
print(s.longestSubarray([-7, -4], 5))
