class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, -float('inf'), -float('inf')]
        for n in nums:
            a, b, c = dp
            dp[(n % 3)] = max(dp[(n % 3)], a + n)
            dp[(n + 1) % 3] = max(dp[(n + 1) % 3], b + n)
            dp[(n + 2) % 3] = max(dp[(n + 2) % 3], c + n)
        return dp[0]