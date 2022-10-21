fn main() {
}

pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
    let mut i: usize = 0;
    let mut j: usize = 0;

    while i < (n + m) as usize && j < n as usize {
        if nums1[i] <= nums2[j] { i+= 1; }
        else { 
            nums1.insert(i, nums2[j]);
            i += 1;
            j += 1;
            nums1.pop();
        }
    }
    while nums1.len() > (n + m) as usize { nums1.pop(); }
}
