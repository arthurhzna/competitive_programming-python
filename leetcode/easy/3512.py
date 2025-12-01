class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        r = s % k
        if r == 0:
            return 0
        return r
