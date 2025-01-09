class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        unique_hashes = set()
        n = len(s)
        base = 11
        PRIME = 10 ** 9 + 7
        for i in range(n):
            window = [0] * 10
            rolling_hash = 0
            for j in range(i, n):
                digit = int(s[j])
                window[digit] += 1
                rolling_hash = (base * rolling_hash + digit + 1) % PRIME
                if all(w == 0 or w == max(window) for w in window):
                    unique_hashes.add(rolling_hash)
        return len(unique_hashes)
