def title_to_number(column_title: str) -> int:
    res = 0
    power = 0
    for i in column_title[::-1]:
        res += (ord(i) - 64) * 26 ** power
        power += 1
    return res


print(title_to_number('A'))
print(title_to_number('AB'))
print(title_to_number('ZY'))
