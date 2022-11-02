use std::rc::Rc;
use std::cell::RefCell;
use std::cmp::min;
use std::collections::VecDeque;

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

pub fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    //min_depth_ref(&root)
    // BFS
    match root {
        None => 0,
        Some(node) => {
            let mut depth = 0;
            let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
            queue.push_back(Rc::clone(&node));
            while !queue.is_empty() {
                depth += 1;
                for i in 0..queue.len() {
                    if let Some(v) = queue.pop_front() {
                        match (&v.borrow().left, &v.borrow().right) {
                            (None, None) => return depth,
                            (Some(l), None) => queue.push_back(Rc::clone(&l)),
                            (None, Some(r)) => queue.push_back(Rc::clone(&r)),
                            (Some(l), Some(r)) => {
                                queue.push_back(Rc::clone(&l));
                                queue.push_back(Rc::clone(&r));
                            }
                        }
                    }
                }
            }

            depth
        }
    }
}

fn min_depth_ref(root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
    match root {
        None => 0,
        Some(tree) => {
            match (&tree.borrow().left, &tree.borrow().right) {
                (None, None) => 1,
                (Some(_), None) => 1 + min_depth_ref(&tree.borrow().left),
                (None, Some(_)) => 1 + min_depth_ref(&tree.borrow().right),
                (Some(_), Some(_)) => 1 + min(min_depth_ref(&tree.borrow().left), min_depth_ref(&tree.borrow().right))
            }
        }
    }
}
