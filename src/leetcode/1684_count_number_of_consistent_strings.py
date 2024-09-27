class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(1 if all(c in allowed for c in s) else 0 for s in words)
    