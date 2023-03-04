import math


class Solution:
    def jump(self, nums: list[int]) -> int:
        return self.jump_recursive(nums, 0)

    def jump_recursive(self, nums: list[int], idx: int) -> int:
        n = len(nums)
        if n <= 1 or idx == n - 1:
            return 0
        tmp = [math.inf]
        jump = nums[idx]
        for i in range(1, min(n - idx - 1, jump) + 1):
            tmp.append(1 + self.jump_recursive(nums, idx + i))
        return min(tmp)

    def jump_memoization(self, nums: list[int]) -> int:
        cache = {}

        def jump(i):
            n = len(nums)
            if n == 1 or i == n - 1:
                return 0
            if i in cache:
                return cache[i]
            tmp = [math.inf]
            max_jump = nums[i]
            for j in range(1, min(n - i - 1, max_jump) + 1):
                tmp.append(1 + jump(i + j))
            cache[i] = min(tmp)
            return cache[i]
        return jump(0)

    def jump_dp(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        dp = [0] * n
        dp[n - 1] = 0
        for i in range(n - 2, -1, -1):
            max_jump = nums[i]
            tmp = [math.inf]
            for j in range(1, min(n - i - 1, max_jump) + 1):
                tmp.append(dp[i + j] + 1)
            dp[i] = min(tmp)
        return dp[0]

    def jump_greedy(self, nums: list[int]) -> int:
        answer = 0
        current_end = 0
        current_farthest = 0
        n = len(nums)

        for i in range(n - 1):
            current_farthest = max(current_farthest, i + nums[i])
            if i == current_end:
                answer += 1
                current_end = current_farthest
        return answer


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
print(s.jump([2, 3, 0, 1, 4]))
print(s.jump([1, 2, 0, 1]))
print(s.jump_memoization([2, 3, 1, 1, 4]))
print(s.jump_memoization([2, 3, 0, 1, 4]))
print(s.jump_memoization([1, 2, 0, 1]))
print(s.jump_memoization([5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8,
                          8, 4, 4, 2, 0, 3, 8, 5]))
print(s.jump_dp([2, 3, 1, 1, 4]))
print(s.jump_dp([2, 3, 0, 1, 4]))
print(s.jump_dp([1, 2, 0, 1]))
print(s.jump_dp([5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4,
                 2, 0, 3, 8, 5]))
print(s.jump_greedy([2, 3, 1, 1, 4]))
print(s.jump_greedy([2, 3, 0, 1, 4]))
print(s.jump_greedy([1, 2, 0, 1]))
print(s.jump_greedy([5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4,
                     4, 2, 0, 3, 8, 5]))
