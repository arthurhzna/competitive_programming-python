class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        mod = 0
        for bit in nums:
            mod = (mod * 2 + bit) % 5
            res.append(mod == 0)
        return res
