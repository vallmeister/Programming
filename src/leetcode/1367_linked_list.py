# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return False
            elif self.start_path(node, head):
                return True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
        
    def start_path(self, tree_node, list_node):
        if not list_node:
            return True
        elif not tree_node:
            return False
        elif list_node.val != tree_node.val:
            return False
        tmp = False
        tmp |= self.start_path(tree_node.left, list_node.next)
        tmp |= self.start_path(tree_node.right, list_node.next)
        return tmp
