class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {letter: val for val, letter in enumerate(order)}
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if letter in order:
                continue
            order_dict[letter] = 27
        return ''.join(sorted(s, key=lambda letter: order_dict[letter]))


print(Solution().customSortString('cba', 'abcd'))
