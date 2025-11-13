class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        cnt1 = nums.count(1)
        if cnt1:
            return n - cnt1
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            if g == 1:
                min_len = 1
                break
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        if min_len == float('inf'):
            return -1
        return (min_len - 1) + (n - 1)