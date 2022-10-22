// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

fn main() {

}

pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut last_value = i32::MIN;
    let mut result_list = ListNode::new(0);
    let mut result_list_iterator = &mut result_list;
    let mut head_iterator = head.as_ref();

    while let Some(node) = head_iterator {
        if node.val != last_value {
            result_list_iterator.next = Some(Box::new(ListNode::new(node.val)));
            result_list_iterator = result_list_iterator.next.as_mut().unwrap();
            last_value = node.val;
        }
        head_iterator = node.next.as_ref();
    }
    result_list.next
}
