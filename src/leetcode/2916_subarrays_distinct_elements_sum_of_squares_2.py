from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        seg = [0] * (4 * n)
        seg_square = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, start, end):
            if lazy[node] == 0:
                return
            seg_square[node] += (end - start + 1) * lazy[node] * lazy[node] + 2 * lazy[node] * seg[node]
            seg[node] += (end - start + 1) * lazy[node]
            if start != end:
                lazy[2 * node] += lazy[node]
                lazy[2 * node + 1] += lazy[node]
            lazy[node] = 0

        def update(node, start, end, l, r):
            push(node, start, end)

            if r < start or end < l:
                return
            elif l <= start and end <= r:
                seg_square[node] += (end - start + 1) + 2 * seg[node]
                seg[node] += (end - start + 1)
                if start != end:
                    lazy[2 * node] += 1
                    lazy[2 * node + 1] += 1
                return
            mid = (start + end) // 2
            update(2 * node, start, mid, l, r)
            update(2 * node + 1, mid + 1, end, l, r)
            seg[node] = (seg[2 * node] + seg[2 * node + 1])
            seg_square[node] = (seg_square[2 * node] + seg_square[2 * node + 1])

        prev_idx = {}
        ans = 0
        for i in reversed(range(n)):
            num = nums[i]
            if num not in prev_idx:
                update(1, 1, n, i + 1, n)
            else:
                j = prev_idx[num]
                update(1, 1, n, i + 1, j)
            prev_idx[num] = i
            ans += seg_square[1]

        return ans % MOD


s = Solution()
print(s.sumCounts(nums=[1, 2, 1]))
print(s.sumCounts(nums=[2, 2]))
print(s.sumCounts([5, 2, 4, 2, 1, 3, 2, 4, 3, 1]))
