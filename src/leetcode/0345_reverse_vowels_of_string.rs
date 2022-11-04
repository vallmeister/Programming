fn main() {
    println!("{}", reverse_vowels("hello".to_string()));
    println!("{}", reverse_vowels("leetcode".to_string()));
    println!("{}", reverse_vowels("aA".to_string()));
}

pub fn reverse_vowels(s: String) -> String {
    let n: usize = s.len();

    let mut i: usize = 0;
    let mut j: usize = n - 1;
    let mut characters: Vec<char> = s.chars().collect();

    let is_vowel = |x: char| x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u'
        || x == 'A' || x == 'E' || x == 'I' || x == 'O' || x == 'U';

    while i < j {
        if is_vowel(characters[i]) && is_vowel(characters[j]) {
            let tmp = characters[i];
            characters[i] = characters[j];
            characters[j] = tmp;

            i += 1;
            j -= 1;
        }

        if !is_vowel(characters[i]) { i += 1; }
        if !is_vowel(characters[j]) { j -= 1; }
    }
    characters.iter().collect()
}