package Programming.leetcode;

import Programming.leetcode.util.TreeNode;

public class PathSum {
  public boolean hasPathSum(TreeNode root, int targetSum) {
    if (root == null) return false;
    else if (root.left == null && root.right == null) return root.val == targetSum;
    else if (root.right == null) return hasPathSum(root.left, targetSum - root.val);
    else if (root.left == null) return hasPathSum(root.right, targetSum - root.val);
    else return hasPathSum(root.left, targetSum - root.val)
              || hasPathSum(root.right, targetSum - root.val);
  }
}
