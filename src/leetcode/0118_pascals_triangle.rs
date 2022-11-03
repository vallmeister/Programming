fn main() {
    println!("{:?}", generate(1));
    println!("{:?}", generate(5));
}

pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
    let mut triangle: Vec<Vec<i32>> = Vec::new();
    triangle.push(vec![1]);
    for i in 1..num_rows {
        let mut row: Vec<i32> = Vec::new();
        row.push(1);
        for j in 1..i {
            row.push(
              triangle[(i-1) as usize][(j-1) as usize] + triangle[(i-1) as usize][j as usize]
            );
        }
        row.push(1);
        triangle.push(row);
    }

    triangle
}