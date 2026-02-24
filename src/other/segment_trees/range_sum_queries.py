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
        self.push()
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

    def push(self):
        if self.lazy:
            self.range_sum += (self.end - self.start + 1) * self.lazy
            if self.left:
                self.left.lazy += self.lazy
            if self.right:
                self.right.lazy += self.lazy
            self.lazy = 0

    def update_range(self, query_start, query_end, val):
        self.push()
        if self.start > query_end or self.end < query_start:
            return
        elif query_start <= self.start and self.end <= query_end:
            self.range_sum += (self.end - self.start + 1) * val
            self.push()
            return
        self.range_sum = 0
        if self.left:
            self.left.update_range(query_start, query_end, val)
            self.range_sum += self.left.range_sum
        if self.right:
            self.right.update_range(query_start, query_end, val)
            self.range_sum += self.right.range_sum


def bfs(root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        if not node:
            continue
        print(f'sum: {node.range_sum}, lazy: {node.lazy}')
        q.append(node.left)
        q.append(node.right)


if __name__ == "__main__":
    arr = [1, 4, 5, 9, 10, 12]
    print(f'Segment tree for range sum and update queries on A:={arr}')
    tree_root = SegmentTreeNode(arr, 0, len(arr) - 1)
    print(f'Range sum from {2} to {4} is {tree_root.get_range_sum(2, 4)}')
    tree_root.update_range(1, 3, 100)
    # bfs(tree_root)
    print(
        f'Range sum from {1} to {3} after adding {100} to each value in the interval is {tree_root.get_range_sum(1, 3)}')
    # bfs(tree_root)
    print(f'Range sum from {2} to {4} is {tree_root.get_range_sum(2, 4)}')
    # bfs(tree_root)
    print(f'Range sum from {4} to {5} is {tree_root.get_range_sum(4, 5)}')
    for i in range(6):
        print(f'arr[{i}] = {tree_root.get_range_sum(i, i)}')
