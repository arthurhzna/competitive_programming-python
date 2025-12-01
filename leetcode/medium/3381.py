class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        best = float('-inf')
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0

        for i, num in enumerate(nums, 1):
            prefix += num
            r = i % k
            best = max(best, prefix - min_prefix[r])
            min_prefix[r] = min(min_prefix[r], prefix)

        return best