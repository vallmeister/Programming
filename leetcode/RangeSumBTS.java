package Coding.LeetCode;

import Coding.LeetCode.util.TreeNode;

public class RangeSumBTS {

  public static void main(String[] args) {
    TreeNode first = new TreeNode(10, new TreeNode(5, new TreeNode(3, new TreeNode(1), null), new TreeNode(7, new TreeNode(6, null, null), null)),
            new TreeNode(15, new TreeNode(13, null, null), new TreeNode(18, null, null)));

    System.out.println(rangeSumBST(first, 6, 10));
  }

  public static int rangeSumBST(TreeNode root, int low, int high) {
    if (root == null) return 0;

    int value = root.val;
    if (value < low) return rangeSumBST(root.right, low, high);
    else if (value > high) return rangeSumBST(root.left, low, high);
    else { // low <= root.value <= high
      return value + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low,high);
    }
  }
}
