use std::rc::Rc;
use std::cell::RefCell;
use std::cmp;

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}

fn main() {}

pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
    is_balanced_ref(&root)
}

fn get_height(root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
    match root {
        None => 0,
        Some(tree) => {
            1 + cmp::max(get_height(&tree.borrow().left), get_height(&tree.borrow().right))
        }
    }
}

fn is_balanced_ref(root: &Option<Rc<RefCell<TreeNode>>>) -> bool {
    match root {
        None => true,
        Some(tree) => {
            (get_height(&tree.borrow().left) - get_height(&tree.borrow().right)).abs() <= 1
                && is_balanced_ref(&tree.borrow().left)
                && is_balanced_ref(&tree.borrow().right)
        }
    }
}
