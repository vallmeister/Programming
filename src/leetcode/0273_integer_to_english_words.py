from collections import deque


class Solution:
    def thousands_to_word(self, num):
        ans = ''
        if num == 0:
            return ans
        units = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty",
                 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        if num // 100 > 0:
            ans += units[num // 100] + " Hundred"
        tens = num % 100
        if tens > 0:
            if tens < 20 or tens % 10 == 0:
                ans += f" {units[tens]}"
            else:
                ones = tens % 10
                ans += f" {units[tens - ones]}" + (f" {units[ones]}" if ones > 0 else "")
        return ans

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ans = deque()
        for group in ["", "Thousand", "Million", "Billion"]:
            tmp = self.thousands_to_word(num % 1000)
            if tmp:
                ans.appendleft(f"{tmp} {group}")
            num //= 1000
        return " ".join(ans).strip().replace("  ", " ")
