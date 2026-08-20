from typing import List


class SegmentTree:

    def __init__(self, n):
        self.n = n
        self.tree = [0] * 4 * n

    def _range_sum_util(self, i, start, end, qs, qe):
        if qe < start or qs > end:
            return 0
        elif qs <= start and end <= qe:
            return self.tree[i]
        else:
            # self._push(i, start, end)
            mid = (start + end) // 2
            return self._range_sum_util(2 * i, start, mid, qs, qe) + self._range_sum_util(2 * i + 1, mid + 1, end, qs,
                                                                                          qe)

    def greater_count(self, rank):
        return self._range_sum_util(1, 0, self.n - 1, rank + 1, self.n)

    def _update_util(self, i, start, end, rank):
        if end < rank or start > rank:
            return
        elif start == end:
            self.tree[i] += 1
        else:
            mid = (start + end) // 2
            self._update_util(2 * i, start, mid, rank)
            self._update_util(2 * i + 1, mid + 1, end, rank)
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def add(self, rank):
        self._update_util(1, 0, self.n - 1, rank)


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rank_of = {v: k for k, v in enumerate(sorted(nums))}

        tree1 = SegmentTree(n)
        tree2 = SegmentTree(n)

        arr1 = [nums[0]]
        tree1.add(rank_of[nums[0]])

        arr2 = [nums[1]]
        tree2.add(rank_of[nums[1]])

        for num in nums[2:]:
            rank = rank_of[num]
            greater_count1 = tree1.greater_count(rank)
            greater_count2 = tree2.greater_count(rank)
            if greater_count1 > greater_count2:
                arr1.append(num)
                tree1.add(rank)
            elif greater_count2 > greater_count1:
                arr2.append(num)
                tree2.add(rank)
            else:
                if len(arr1) <= len(arr2):
                    arr1.append(num)
                    tree1.add(rank)
                else:
                    arr2.append(num)
                    tree2.add(rank)
        return arr1 + arr2


s = Solution()
print(s.resultArray(nums=[2, 1, 3, 3]))
print(s.resultArray(nums=[5, 14, 3, 1, 2]))
print(s.resultArray(nums=[3, 3, 3, 3]))
