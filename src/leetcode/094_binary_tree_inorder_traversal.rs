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
//impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        match root {
            Some(node) => {
                let mut result: Vec<i32> = Vec::new();
                // left traversal
                let mut lft: Vec<i32> = if let Some(l) = &node.borrow().left {
                    Self::inorder_traversal(Some(Rc::clone(&l)))
                } else {
                    Vec::new()
                };
                result.append(&mut lft);

                result.push(node.borrow().val);
                
                // right traversal
                let mut rgt = if let Some(r) = &node.borrow().right {
                    Self::inorder_traversal(Some(Rc::clone(&r)))
                } else {
                    Vec::new()
                };
                result.append(&mut rgt);
                result
            },
            None => { return Vec::new(); }
        }
    }
//}
