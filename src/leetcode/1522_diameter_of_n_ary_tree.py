# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        max_diameter = 0

        def find_diameter(node):
            nonlocal max_diameter
            fst = 0
            snd = 0
            for child in node.children:
                depth = find_diameter(child)
                if depth > fst:
                    fst, snd = depth, fst
                elif depth > snd:
                    snd = depth
            if snd > 0:
                max_diameter = max(max_diameter, fst + snd)
            elif fst > 0:
                max_diameter = max(max_diameter, fst)
            return fst + 1

        find_diameter(root)
        return max_diameter
