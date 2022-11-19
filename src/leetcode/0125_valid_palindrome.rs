fn main() {
    println!("{}", is_palindrome("A man, a plan, a canal: Panama".to_string()));
    println!("{}", is_palindrome(" ".to_string()));
    println!("{}", is_palindrome("rentne".to_string()));

}

pub fn is_palindrome(s: String) -> bool {
    let tmp: String = s.to_lowercase().chars().filter(|c| c.is_alphanumeric()).collect();
    let tmp: Vec<char> = tmp.chars().collect();
    if tmp.len() < 2 { return true; }
    let mut i = 0;
    let mut j = tmp.len() - 1;

    while i < j {
        if tmp[i] != tmp[j] { return false; }
        i += 1;
        j -= 1;
    }

    true
}
