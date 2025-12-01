class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        r = total % p
        if r == 0:
            return 0

        prefix = 0
        seen = {0: -1}    
        res = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - r) % p

            if target in seen:
                res = min(res, i - seen[target])

            seen[prefix] = i

        return res if res < len(nums) else -1
