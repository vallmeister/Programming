class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        tree = self.get_tree(parent)

        def get_height(node):
            h = 0
            for child in tree[node]:
                h = max(h, get_height(child))
            return h + 1

        height = get_height(0)

        def dfs(node, depth):
            ans = nums[node] * (height - depth + 1)
            for child in tree[node]:
                ans += dfs(child, depth + 1)
            return ans

        return dfs(0, 1)

    def get_tree(self, parent):
        n = len(parent)
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)
        return tree


s = Solution()
print(s.weightedSum(parent=[-1, 0, 0, 0, 2, 2], nums=[5, 2, 3, 1, 4, 6]))
print(s.weightedSum(parent=[-1, 0, 1, 2], nums=[1, 2, 3, 4]))
