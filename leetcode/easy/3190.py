class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            r = n % 3
            if r != 0:
                res += min(r, 3 - r)
        return res