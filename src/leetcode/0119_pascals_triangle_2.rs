fn main() {
    println!("{:?}", get_row(0));
    println!("{:?}", get_row(1));
    println!("{:?}", get_row(2));
    println!("{:?}", get_row(3));
    println!("{:?}", get_row(4));
    println!("{:?}", get_row(5));
}

pub fn get_row(row_index: i32) -> Vec<i32> {
    if row_index == 0 { return vec![1]; }
    let mut previous: Vec<i32> = vec![1,1];

    for i in 1..=row_index {
        let mut new: Vec<i32> = vec![1];
        for j in 1..i {
            new.push(previous[(j-1) as usize] + previous[j as usize]);
        }
        new.push(1);
        previous = new;
    }
    previous
}
