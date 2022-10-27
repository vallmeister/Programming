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

use std::rc::Rc;
use std::cell::RefCell;

pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
    match root {
        None => { true },
        Some(node) => { is_mirror(node.borrow().left.clone(), node.borrow().right.clone()) }
    }
}

pub fn is_mirror(tree1: Option<Rc<RefCell<TreeNode>>>, tree2: Option<Rc<RefCell<TreeNode>>>) -> bool {
    match (tree1, tree2) {
        (None, None) => { true },
        (Some(t1), Some(t2)) => {
            t1.borrow().val == t2.borrow().val
                && is_mirror(t1.borrow().left.clone(), t2.borrow().right.clone())
                && is_mirror(t1.borrow().right.clone(), t2.borrow().left.clone())
        }
        (_, _) => { false }
    }
}