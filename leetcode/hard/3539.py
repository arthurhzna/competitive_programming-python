from typing import List

MOD = 10**9 + 7

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        L = n + 31  
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i-1] * i % MOD
        invfact = [1] * (m + 1)
        invfact[m] = pow(fact[m], MOD-2, MOD)
        for i in range(m, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD
        pow_nums = [[1] * (m + 1) for _ in range(L)]
        for pos in range(L):
            if pos < n:
                a = nums[pos] % MOD
                for c in range(1, m + 1):
                    pow_nums[pos][c] = pow_nums[pos][c-1] * a % MOD
            else:
                for c in range(1, m + 1):
                    pow_nums[pos][c] = 0  
        from itertools import product
        cur = [[[0] * (k+1) for _ in range(m+1)] for __ in range(m+1)]
        cur[0][0][0] = 1
        for pos in range(L):
            nxt = [[[0] * (k+1) for _ in range(m+1)] for __ in range(m+1)]
            for carry in range(0, m+1):
                for used in range(0, m+1):
                    row = cur[carry][used]
                    if all(v == 0 for v in row):
                        continue
                    maxc = m - used if pos < n else 0
                    for c in range(0, maxc + 1):
                        add_pow = pow_nums[pos][c] 
                        if add_pow == 0 and c > 0:
                            continue
                        coef = invfact[c] 
                        mul = add_pow * coef % MOD
                        for ones in range(0, k+1):
                            val = row[ones]
                            if val == 0:
                                continue
                            sum_ = c + carry
                            bit = sum_ & 1
                            ones2 = ones + bit
                            if ones2 > k:
                                continue
                            carry2 = sum_ >> 1
                            nxt[carry2][used + c][ones2] = (nxt[carry2][used + c][ones2] + val * mul) % MOD
            cur = nxt
        res_coeff = cur[0][m][k]  
        ans = res_coeff * fact[m] % MOD
        return ans
