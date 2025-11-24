class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        suffix = [0] * 26
        for ch in s:
            suffix[ord(ch) - 97] += 1

        prefix = [False] * 26
        found = set()