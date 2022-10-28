#![allow(dead_code)]
#![allow(unused_imports)]
#![allow(unused_must_use)]

use std::collections::HashSet;

fn main() {

}

pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
    let mut result: Vec<i32> = Vec::new();
    let n: i32 = nums.len() as i32;
    let mut all_nums = HashSet::new();

    for i in nums {
        if all_nums.contains(&i) {
            result.push(i);
        } else {
            all_nums.insert(i);
        }
    }

    for i in 1..=n { 
        if !all_nums.contains(&i) { result.push(i); }
     }
    
    result
}