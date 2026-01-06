from typing import List


class SegmentTree:

    def __init__(self, size):
        self.size = size
        self.tree = [0] * (4 * size)

    def update(self, node, start, end, idx):
        if start == end:
            self.tree[node] = 1
            return

        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx)
        else:
            self.update(2 * node + 1, mid + 1, end, idx)

        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        elif l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return p1 + p2


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ordered_ratings = sorted(rating)
        rating_to_idx = {r: i for i, r in enumerate(ordered_ratings)}

        st_left = SegmentTree(n)
        left_smaller = [0] * n
        left_greater = [0] * n
        for i in range(n):
            curr_rating = rating_to_idx[rating[i]]
            left_smaller[i] = st_left.query(node=1, start=0, end=n - 1, l=0, r=curr_rating - 1)
            left_greater[i] = st_left.query(node=1, start=0, end=n - 1, l=curr_rating + 1, r=n - 1)
            st_left.update(node=1, start=0, end=n - 1, idx=curr_rating)

        st_right = SegmentTree(n)
        right_smaller = [0] * n
        right_greater = [0] * n
        for i in reversed(range(n)):
            curr_rating = rating_to_idx[rating[i]]
            right_greater[i] = st_right.query(node=1, start=0, end=n - 1, l=curr_rating + 1, r=n - 1)
            right_smaller[i] = st_right.query(node=1, start=0, end=n - 1, l=0, r=curr_rating - 1)
            st_right.update(node=1, start=0, end=n - 1, idx=curr_rating)

        ans = 0
        for i in range(n):
            ans += left_smaller[i] * right_greater[i]
            ans += left_greater[i] * right_smaller[i]
        return ans


s = Solution()
print(s.numTeams(rating=[2, 5, 3, 4, 1]))
print(s.numTeams(rating=[2, 1, 3]))
print(s.numTeams(rating=[1, 2, 3, 4]))
