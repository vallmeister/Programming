fn main() {

}

struct StockSpanner {
    monotonic_stack: Vec<(i32, i32)>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StockSpanner {

    fn new() -> Self {
        StockSpanner { monotonic_stack: Vec::new() }
    }
    
    fn next(&mut self, price: i32) -> i32 {
        let mut ans = 1;
        while self.monotonic_stack.len() > 0 {
            let (p, days) = self.monotonic_stack.pop().unwrap();
            if p > price { 
                self.monotonic_stack.push((p, days)); 
                break;
            } else {
                ans += days;
            }
        }
        self.monotonic_stack.push((price, ans));
        ans
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * let obj = StockSpanner::new();
 * let ret_1: i32 = obj.next(price);
 */
