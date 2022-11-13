fn main() {
    println!("{}", reverse_words(" test hello ".to_string()));
}

pub fn reverse_words(s: String) -> String {
    let mut words: Vec<&str> = s.split_whitespace().collect();
    let mut result = String::new();

    for i in 0..words.len() { 
        result.push_str(words.pop().unwrap());
        result.push_str(" ");
    }
    
    result.trim().to_string()
}
