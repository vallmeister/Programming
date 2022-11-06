fn main() {
    println!("{}", max_profit(vec![7,1,5,3,6,4]));
    println!("{}", max_profit(vec![7,6,4,3,1]));
}

pub fn max_profit(prices: Vec<i32>) -> i32 {
    let mut cheapest = std::i32::MAX;
    let mut profit = 0;
    
    for i in prices {
        if i < cheapest { cheapest = i; }
        let today = i - cheapest;
        if today > profit { profit = today; }
    }
    profit
}
