class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0

        for row in bank:
            cur = row.count('1')
            if cur > 0:
                ans += prev * cur
                prev = cur
        
        return ans
