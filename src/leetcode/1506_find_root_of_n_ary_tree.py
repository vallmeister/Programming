# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        not_root = set()
        for node in tree:
            for child in node.children:
                not_root.add(child)
        tree = set(tree)
        tree = tree - not_root
        return tree.pop()
