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

pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool {
    match p {
        None => {
            match q {
                None => { true },
                _ => { false }
            }
        },
        Some(t1) => {
            match q {
                None => { false },
                Some(t2) => {
                    let left1 = if let Some(l1) = &t1.borrow().left {
                        Some(Rc::clone(&l1))
                    } else {
                        None
                    };
                    let left2 = if let Some(l2) = &t2.borrow().left {
                        Some(Rc::clone(&l2))
                    } else {
                        None
                    };
                    let right1 = if let Some(r1) = &t1.borrow().right {
                        Some(Rc::clone(&r1))
                    } else {
                        None
                    };
                    let right2 = if let Some(r2) = &t2.borrow().right {
                        Some(Rc::clone(&r2))
                    } else {
                        None
                    };
                    t1.borrow().val == t2.borrow().val
                    && Self::is_same_tree(left1, left2)
                    && Self::is_same_tree(right1, right2)
                }
            }
        }
    }
}
