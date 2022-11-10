fn main() {
    println!("{}", remove_duplicates("abbaca".to_string()));
    println!("{}", remove_duplicates("azxxzy".to_string()));
    println!("{}", remove_duplicates("a".to_string()));
    println!("{}", remove_duplicates("aa".to_string()));
    println!("{}", remove_duplicates("aab".to_string()));
}

use std::cmp::max;

pub fn remove_duplicates(s: String) -> String {
    let mut stack = Vec::new();

    for c in s.chars() {
        if let Some(last) = stack.last() {
            if *last == c { stack.pop(); }
            else { stack.push(c); }
        } else { stack.push(c); }
    }

    stack.iter().collect()
}
