//use std::collections::HashSet;

fn main() {}

pub fn is_toeplitz_matrix(matrix: Vec<Vec<i32>>) -> bool {
    let m = matrix.len();
    let n = matrix[0].len();

    // check every column from 0 to n starting at column 0
    for i in 0..n {
        let mut line = 0;
        let mut column = i;
        //let mut elements: HashSet<i32> = HashSet::new();
        let element = matrix[line][column];
        while line < m && column < n {
            //elements.insert(matrix[line][column]);
            if matrix[line][column] != element { return false; }
            line += 1;
            column += 1;
        }
        //if elements.len() > 1 { return false; }
    }

    // check every line from 1 to m starting at line 1
    for i in 1..m {
        let mut line = i;
        let mut column = 0;
        //let mut elements: HashSet<i32> = HashSet::new();
        let element = matrix[line][column];
        while line < m && column < n {
            //elements.insert(matrix[line][column]);
            if matrix[line][column] != element { return false; }
            line += 1;
            column += 1;
        }
        //if elements.len() > 1 { return false; }
    }
    true
}