use std::cmp;
use std::collections::HashMap;

fn main() {
    println!("{}", contains_nearby_duplicate(vec![1,2,3,1], 3));
    println!("{}", contains_nearby_duplicate(vec![1,0,1,1], 1));
    println!("{}", contains_nearby_duplicate(vec![1,2,3,1,2,3], 2));
    println!("{}", contains_nearby_duplicate(vec![99,99], 2));
}

// Time: O(n*k)
// Space: O(1)
pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
    for i in 0..(nums.len() as i32) {
        for j in (i+1)..cmp::min(i + k + 1, nums.len() as i32) {
            if nums[i as usize] == nums[j as usize] && i != j { return true; }
        }
    }

    return false;
}

// Time: O(n)
// Space: O(n)
pub fn contains_nearby_duplicate_optimized(nums: Vec<i32>, k: i32) -> bool {
    let mut lookup: HashMap<i32,i32> = HashMap::new();
    for i in 0..(nums.len() as i32) {
        if lookup.contains_key(&nums[i as usize]) {
            match lookup.get(&nums[i as usize]) {
                Some(z) => if i - z <= k { return true; },
                None => continue
            }
        }
        lookup.insert(nums[i as usize], i);
    }
    return false;
}
