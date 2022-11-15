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

fn main() {}

pub fn count_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    if let None = root { return 0; }

    dfs(&root)
}

fn dfs(root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
    if let Some(v) = root { return 1 + dfs(&v.borrow().left) + dfs(&v.borrow().right) }
    else { return 0 }
}

fn subtree_parity(root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
    if let None = root { return 0; }

    let l = dfs_left(&root);
    let r = dfs_right(&root);

    if l == r { return (1 << l) - 1}

    1 + subtree_parity(&root.as_ref().unwrap().borrow().left) + subtree_parity(&root.as_ref().unwrap().borrow().right)
}

fn dfs_left(left: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
  if let None = left { return 0; }
  1 + dfs_left(&left.as_ref().unwrap().borrow().left)
}

fn dfs_right(right: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
  if let None = right { return 0; }
  1 + dfs_right(&right.as_ref().unwrap().borrow().right)
}
