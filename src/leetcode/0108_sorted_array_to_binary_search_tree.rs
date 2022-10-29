// #[derive(Debug, PartialEq, Eq)]
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
            right: None,
        }
    }
}
use std::cell::RefCell;
use std::rc::Rc;

fn main() {}

pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
    if nums.len() == 0 {
        return None;
    }
    let mid: usize = nums.len() / 2;
    let mut root = TreeNode::new(nums[mid]);
    {
        let mut left_nums = Vec::new();
        for i in &nums[0..mid] {
            left_nums.push(*i);
        }
        if let Some(left) = sorted_array_to_bst(left_nums) {
            root.left = Some(Rc::clone(&left));
        }
    }
    {
        let mut right_nums = Vec::new();
        for i in &nums[mid + 1..nums.len()] {
            right_nums.push(*i);
        }
        if let Some(right) = sorted_array_to_bst(right_nums) {
            root.right = Some(Rc::clone(&right));
        }
    }
    Some(Rc::new(RefCell::new(root)))
}
