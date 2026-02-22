from collections import deque


class SegmentTreeNode:

    def __init__(self, nums, start, end):
        self.arr = nums
        self.range_sum = 0
        self.lazy = 0
        self.start = start
        self.end = end
        self.left = self.right = None
        if start == end:
            self.range_sum = nums[start]
        else:
            mid = (start + end) // 2
            self.left = SegmentTreeNode(nums, start, mid)
            self.right = SegmentTreeNode(nums, mid + 1, end)
            self.range_sum = self.left.range_sum + self.right.range_sum

    def get_range_sum(self, query_start, query_end):
        if self.end < query_start or self.start > query_end:
            return 0
        elif query_start <= self.start and self.end <= query_end:
            return self.range_sum
        ans = 0
        if self.left:
            ans += self.left.get_range_sum(query_start, query_end)
        if self.right:
            ans += self.right.get_range_sum(query_start, query_end)
        return ans


def bfs(root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        if not node:
            continue
        print(node.range_sum)
        q.append(node.left)
        q.append(node.right)


if __name__ == "__main__":
    arr = [1, 4, 5, 9, 10, 12]
    print(f'Segment tree for range sum and update queries on A:={arr}')
    tree_root = SegmentTreeNode(arr, 0, len(arr) - 1)
    # bfs(tree_root)
    qs, qe = 2, 4
    print(f'Range sum from {qs} to {qe} is {tree_root.get_range_sum(qs, qe)}')
