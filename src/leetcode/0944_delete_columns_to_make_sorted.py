def minDeletionSize(strs: list[str]) -> int:
    result = 0
    for i in range(len(strs[0])):
        for j in range(len(strs) - 1):
            if strs[j][i] > strs[j + 1][i]:
                result += 1
                break
    return result


def min_deletion_one_line(strs: list[str]) -> int:
    return sum(list(i) != sorted(i) for i in zip(*strs))


print(minDeletionSize(["abc", "bce", "cae"]))
print(minDeletionSize(["a", "b"]))
print(minDeletionSize(["cba", "daf", "ghi"]))
print(minDeletionSize(["zyx", "wvu", "tsr"]))
print(min_deletion_one_line(["zyx", "wvu", "tsr"]))

