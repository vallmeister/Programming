class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        ans = 0
        while full > 0 or empty >= numExchange:
            ans += full
            empty += full
            full = empty // numExchange
            empty %= numExchange
        return ans
