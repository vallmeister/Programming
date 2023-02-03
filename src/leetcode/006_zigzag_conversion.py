def convert(s: str, num_rows: int) -> str:
    rows = []
    for _ in range(num_rows):
        rows.append([])
    current_row = 0
    factor = 1
    for letter in s:
        rows[current_row].append(letter)
        current_row += factor
        if current_row >= num_rows:
            current_row -= 2
            factor = -1
        elif current_row < 0:
            current_row += 2
            factor = 1
    print(rows)
    return ''.join([''.join(i) for i in rows])


print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))
print(convert("A", 4))
print(convert("PAYPALISHIRING", 1))
