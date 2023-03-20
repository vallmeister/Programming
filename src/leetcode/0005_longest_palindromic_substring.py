class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.longest_palindrome_dp(s)

    def longest_palindrome_dp(self, s):
        longest_so_far = ''
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j + 1):
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
                if dp[i][j] and len(longest_so_far) < j - i + 1:
                    longest_so_far = s[i:j + 1]
        return longest_so_far

    def longest_palindrome_brute_force(self, s):
        longest_so_far = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                s1 = s[i:j]
                if s1 == s1[::-1] and len(longest_so_far) < len(s1):
                    longest_so_far = s1
        return longest_so_far


sol = Solution()
print(sol.longest_palindrome_brute_force('babad'))
print(sol.longest_palindrome_brute_force('cbbd'))
print(sol.longest_palindrome_dp('babad'))
print(sol.longest_palindrome_dp('cbbd'))
print(sol.longest_palindrome_dp(
    'wgjtmwgpfnoeisdozatlhfvcqzlsffkoxrsdjhryqtppdeqrkjabodgtmkthwmtmerxlazsfdogsrwtswhbqclpcagfjlfuyvsnummfjmmxpdhupwkztnwcbppbbwfnwfaoazmautdiutzkwfqibglhypfamgxzsfctapkjimmyazulehprmzfvhaxzbobhvsbxscimjnmibivwbenfrhsudmpmkkbphjyrgjficjvfosrnhdsnjqtaycmyorpujyloozeeinqfsesuauqmsxmoafoszqrzbgechluecfdxulmcxxbiqvqkohlgqlqxierzbyradeoebbdhyjdkiaezfphfetiyelelunryvmczewjwkfrgjvdbouorqymmamkonncostamlpyrxoxnccbilnqdqbeieqncitfgitluvzxildtsiaipbskicepbvhtfdgxfiyywznzdstzvayjmwvlolhtvpekyakajeixdjkbbdlttldbbkjdxiejakaykepvthlolvwmjyavztsdznzwyyifxgdfthvbpeciksbpiaistdlixzvultigfticnqeiebqdqnlibccnxoxryplmatsocnnokmammyqrouobdvjgrfkwjwezcmvyrnuleleyitefhpfzeaikdjyhdbbeoedarybzreixqlqglhokqvqibxxcmluxdfceulhcegbzrqzsofaomxsmquausesfqnieezoolyjuproymcyatqjnsdhnrsofvjcifjgryjhpbkkmpmdushrfnebwvibimnjmicsxbsvhbobzxahvfzmrpheluzaymmijkpatcfszxgmafpyhlgbiqfwkztuidtuamzaoafwnfwbbppbcwntzkwpuhdpxmmjfmmunsvyufljfgacplcqbhwstwrsgodfszalxremtmwhtkmtgdobajkrqedpptqyrhjdsrxokffslzqcvfhltazodsieonfpgwmtjgw'))
