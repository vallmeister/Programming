# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        clones = {}

        def clone(root):
            if root not in clones:
                clones[root] = Node(root.val)
                for neighbor in root.neighbors:
                    clone(neighbor)

        clone(node)

        for original in clones:
            for neighbor in original.neighbors:
                clones[original].neighbors.append(clones[neighbor])
        return clones[node]
