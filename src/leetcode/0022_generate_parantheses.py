class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        parenthesis = []

        def generate(curr_parenthesis, left_open, left_closed):
            if left_open == 0 and left_closed == 0:
                parenthesis.append(curr_parenthesis)
            elif left_open == 0:
                generate(curr_parenthesis + ')', left_open, left_closed - 1)
            elif left_open == left_closed:
                generate(curr_parenthesis + '(', left_open - 1, left_closed)
            else:
                generate(curr_parenthesis + '(', left_open - 1, left_closed)
                generate(curr_parenthesis + ')', left_open, left_closed - 1)

        generate('', n, n)
        return parenthesis


s = Solution()
print(s.generateParenthesis(3))
print(s.generateParenthesis(1))
