fn main() {
    println!("{}", increasing_triplet(vec![1,2,3,4,5]));
    println!("{}", increasing_triplet(vec![5,4,3,2,1]));
    println!("{}", increasing_triplet(vec![2,1,5,0,4,6]));

}

pub fn increasing_triplet(nums: Vec<i32>) -> bool {
    if nums.len() < 3 {return false};
    let mut max1 : i32 = std::i32::MAX;
    let mut max2 : i32 = std::i32::MAX;

    for i in 0..nums.len() {
        let tmp : i32 = nums[i];
        if tmp <= max1 {max1 = tmp}
        else if tmp <= max2 {max2 = tmp}
        else {return true}
    };

    return false;
}
