// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Time: O(n*k), k is length of single strings
// Space: O(n)
use std::collections::HashMap;

fn main() {
    println!(
        "{:?}",
        group_anagrams(vec![
            "eat".into(),
            "tea".into(),
            "tan".into(),
            "ate".into(),
            "nat".into(),
            "bat".into()
        ])
    );
    println!(
        "{:?}",
        group_anagrams(vec!["bdddddddddd".into(), "bbbbbbbbbbc".into()])
    );
}

pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    let mut string_to_anagrams: HashMap<String, Vec<String>> = HashMap::new();

    for string in strs {
        let mut char_count = [0i32; 26];
        for c in string.chars() {
            let index = c as usize - 'a' as usize;
            char_count[index] += 1;
        }
        let mut key = String::new();
        for i in char_count {
            key = format!("{}{}{}", key, i, '-');
        }
        if let Some(l) = string_to_anagrams.remove(&key) {
            let mut list = l;
            list.push(string);
            string_to_anagrams.insert(key, list);
        } else {
            let mut list: Vec<String> = Vec::new();
            list.push(string);
            string_to_anagrams.insert(key, list);
        }
    }
    string_to_anagrams.into_values().collect()
}
