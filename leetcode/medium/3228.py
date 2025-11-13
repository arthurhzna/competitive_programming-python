class Solution:
    def maxOperations(self, s: str) -> int:
        operations = 0
        ones_count = 0

        for i, ch in enumerate(s):
            if ch == '1':
                ones_count += 1
            elif i + 1 == len(s) or s[i + 1] == '1':
                operations += ones_count

        return operations
