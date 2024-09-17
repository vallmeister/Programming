from typing import List


class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        child_parent = {}
        for region in regions:
            parent_node = region[0]
            for child_node in region[1:]:
                child_parent[child_node] = parent_node
        i = j = 0
        path1 = self.find_path(child_parent, region1)
        path2 = self.find_path(child_parent, region2)

        lca = ''
        while i < len(path1) and j < len(path2) and path1[i] == path2[j]:
            lca = path1[i]
            i += 1
            j += 1
        return lca

    def find_path(self, parents, node):
        path = [node]
        while node in parents:
            node = parents[node]
            path.append(node)
        path.reverse()
        return path


s = Solution()
print(s.findSmallestRegion([["Earth", "North America", "South America"], ["North America", "United States", "Canada"],
                            ["United States", "New York", "Boston"], ["Canada", "Ontario", "Quebec"],
                            ["South America", "Brazil"]], "Quebec", "New York"))
print(s.findSmallestRegion([["Earth", "North America", "South America"], ["North America", "United States", "Canada"],
                            ["United States", "New York", "Boston"], ["Canada", "Ontario", "Quebec"],
                            ["South America", "Brazil"]], "Canada", "Quebec"))
