class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        from functools import lru_cache
        n = len(s)
        
        @lru_cache(maxsize=None)
        def dp(i, mask, changed):
            if i == n:
                return 0
            
            char_bit = 1 << (ord(s[i]) - ord('a'))
            new_mask = mask | char_bit
            bits = new_mask.bit_count()
            
            if bits <= k:
                result = dp(i + 1, new_mask, changed)
            else:
                result = 1 + dp(i + 1, char_bit, changed)
            
            if not changed:
                for c in range(26):
                    c_bit = 1 << c
                    if c_bit != char_bit:
                        new_mask2 = mask | c_bit
                        if new_mask2.bit_count() <= k:
                            result = max(result, dp(i + 1, new_mask2, True))
                        else:
                            result = max(result, 1 + dp(i + 1, c_bit, True))
            
            return result
        
        return dp(0, 0, False) + 1