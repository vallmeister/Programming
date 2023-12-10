from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif token == '+':
                summand_2 = stack.pop()
                summand_1 = stack.pop()
                stack.append(summand_1 + summand_2)
            elif token == '-':
                subtrahend = stack.pop()
                minuend = stack.pop()
                stack.append(minuend - subtrahend)
            elif token == '*':
                factor_2 = stack.pop()
                factor_1 = stack.pop()
                stack.append(factor_1 * factor_2)
            elif token == '/':
                denominator = stack.pop()
                nominator = stack.pop()
                result = int(nominator / denominator)
                stack.append(result)
            elif token.startswith('-'):
                stack.append(-1 * int(token[1:]))
        return stack[0]


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
