from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.arr = nums
        self.tree = [0] * (4 * self.n)
        self.lazy = [101] * (4 * self.n)
        self._build(1, 0, self.n - 1)

    def _build(self, i, start, end):
        if start == end:
            self.tree[i] = self.arr[start]
        else:
            mid = (start + end) // 2
            self._build(2 * i, start, mid)
            self._build(2 * i + 1, mid + 1, end)
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def _push(self, i, start, end):
        if self.lazy[i] > 100:
            return
        self.tree[i] = (end - start + 1) * self.lazy[i]
        if start != end:
            self.lazy[2 * i] = self.lazy[i]
            self.lazy[2 * i + 1] = self.lazy[i]
        self.lazy[i] = 101

    def _range_sum_util(self, i, start, end, qs, qe):
        self._push(i, start, end)
        if end < qs or start > qe:
            return 0
        elif qs <= start and end <= qe:
            return self.tree[i]
        mid = (start + end) // 2
        return self._range_sum_util(2 * i, start, mid, qs, qe) + self._range_sum_util(2 * i + 1, mid + 1, end, qs, qe)

    def _range_update_util(self, i, start, end, qs, qe, val):
        if end < qs or qe < start:
            return
        elif qs <= start and end <= qe:
            self.lazy[i] = val
            self._push(i, start, end)
        else:
            mid = (start + end) // 2
            self._range_update_util(2 * i, start, mid, qs, qe, val)
            self._range_update_util(2 * i + 1, mid + 1, end, qs, qe, val)
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        self._range_update_util(1, 0, self.n - 1, index, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self._range_sum_util(1, 0, self.n - 1, left, right)


numbers = [1, 3, 5]
segment_tree = NumArray(numbers)
print(segment_tree.sumRange(0, 2))
segment_tree.update(1, 2)
print(segment_tree.sumRange(0, 2))

print('-' * 50)

segment_tree = NumArray([1, 4, 5, 9, 10, 12])
print(segment_tree.sumRange(2, 4))
segment_tree.update(2, 100)
print(segment_tree.sumRange(2, 5))
