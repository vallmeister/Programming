use std::collections::HashSet;

fn main() {
    println!("{}", contains_duplicate(vec![1,2,3,1]));
    println!("{}", contains_duplicate(vec![1,2,3,4]));
    println!("{}", contains_duplicate(vec![1,1,1,3,3,4,3,2,4,2]));
}

pub fn contains_duplicate(nums: Vec<i32>) -> bool {
    let mut numbers: HashSet<i32> = HashSet::new();
    for i in nums {
        if numbers.contains(&i) { return true; }
        numbers.insert(i);
    }
    return false;
}
