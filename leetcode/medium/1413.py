class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        current = 0
        
        for c in s:
            if c == '1':
                current += 1
            else:
                count = (count + current * (current + 1) // 2) % MOD
                current = 0
        
        count = (count + current * (current + 1) // 2) % MOD
        return count
