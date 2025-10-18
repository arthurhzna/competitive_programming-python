class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr = -10**30
        ans = 0
        for x in nums:
            L = x - k
            R = x + k
            nxt = max(curr + 1, L)
            if nxt <= R:
                curr = nxt
                ans += 1
        return ans
