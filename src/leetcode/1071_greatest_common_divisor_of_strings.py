def gcd_of_strings(str1: str, str2: str) -> str:
    if str1 == str2:
        return str1
    if len(str1) < len(str2):
        tmp = str1
        str1 = str2
        str2 = tmp
    if not str1.startswith(str2):
        return ""
    else:
        return gcd_of_strings(str1[len(str2):], str2)


print(gcd_of_strings("ABCABC", "ABC"))
print(gcd_of_strings("ABABAB", "ABAB"))
print(gcd_of_strings("LEET", "CODE"))
