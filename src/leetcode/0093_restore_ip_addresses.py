def valid_length(s: str, n: int) -> bool:
    return n * 3 >= len(s) > n


def valid_string(s: str) -> bool:
    if "00" in s[:2] or int(s) > 255:
        return False
    return True


def enumerate_possible_addresses(s: str, dots: int) -> list[str]:
    addresses = []
    if dots == 0 and valid_string(s):
        addresses.append(s)
        return addresses
    pass


def restore_ip_address(s: str) -> list[str]:
    n = len(s)
    if n > 12:
        return []
    elif n == 4:
        address = ""
        for i in s:
            address += i
            address += '.'
        return [address[:-1]]
    elif n == 12:
        address = ""
        for i in range(4):
            sub = s[i * 3: (i + 1) * 3]
            if valid_string(sub):
                address += sub
            else:
                return []
            address += '.'
        return [address[:-1]]
    return enumerate_possible_addresses(s, 3)


print(restore_ip_address("25525511135"))
print(restore_ip_address("255255111235"))
print(restore_ip_address("255255111354567897"))
print(restore_ip_address("0000"))
print(restore_ip_address("6020"))
print(restore_ip_address("101023"))
