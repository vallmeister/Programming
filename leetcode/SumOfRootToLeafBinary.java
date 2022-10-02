package Coding.LeetCode;

import Coding.LeetCode.util.TreeNode;

public class SumOfRootToLeafBinary {

  public static int sumRootToLeaf(TreeNode root) {
    return helpSumRootToLeaf(root, 0);
  }

  private static int helpSumRootToLeaf(TreeNode node, int sum) {
    sum += node.val;
    if (node.left == null && node.right == null) return sum;
    else if (node.left == null && node.right != null) return helpSumRootToLeaf(node.right, 2 * sum);
    else if (node.left != null && node.right == null) return helpSumRootToLeaf(node.left, 2 * sum);
    else return helpSumRootToLeaf(node.left, sum * 2) + helpSumRootToLeaf(node.right, 2 * sum);
  }
}
