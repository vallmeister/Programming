class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(corridor)
        total_seats = 0
        curr_group = 0
        curr_plants = 0
        plants = []
        for i in range(n):
            if corridor[i] == 'S':
                total_seats += 1
                curr_group += 1
            if curr_group == 3:
                plants.append(curr_plants + 1)
                curr_group = 1
                curr_plants = 0
            elif curr_group == 2 and corridor[i] == 'P':
                curr_plants += 1
        if total_seats % 2 != 0 or total_seats == 0:
            return 0
        ans = 1
        for num in plants:
            ans *= num
        return ans % MOD


s = Solution()
print(s.numberOfWays("SSPPSPS"))
print(s.numberOfWays("PPSPSP"))
print(s.numberOfWays("S"))
print(s.numberOfWays("SS"))
print(s.numberOfWays("P"))
print(s.numberOfWays("SPPSSSSPPS"))
print(s.numberOfWays("SPSPPSSPSSSS"))
