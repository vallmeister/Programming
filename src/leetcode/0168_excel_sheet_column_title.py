# import string


def convertToTitle(columnNumber: int) -> str:
    res = ""
    # number_to_letter = dict(zip([i for i in range(26)], [i for i in string.ascii_uppercase]))
    while columnNumber > 0:
        columnNumber -= 1
        res += chr(65 + columnNumber % 26)  # number_to_letter[columnNumber % 26]
        columnNumber //= 26

    return res[::-1]


print(convertToTitle(28))
print(convertToTitle(701))
