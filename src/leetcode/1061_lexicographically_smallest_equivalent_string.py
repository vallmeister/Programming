def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    n = len(s1)
    letter_groups = {}
    result = ''
    for i in range(n):
        c1 = s1[i]
        c2 = s2[i]
        group = letter_groups.get(c1, set())
        group = group.union(letter_groups.get(c2, c2))
        group.add(c1)
        group.add(c2)
        for j in group:
            letter_groups[j] = group
    for i in baseStr:
        if i in letter_groups:
            result += min(list(letter_groups[i]))
        else:
            result += i
    return result


print(smallestEquivalentString("parker", "morris", "parser"))
print(smallestEquivalentString("leetcode", "programs", "sourcecode"))
