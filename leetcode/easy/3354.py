class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        s = sum(nums)
        ans = 0
        left = 0
        for x in nums:
            if x != 0:
                left += x
            else:
                if left * 2 == s:
                    ans += 2
                elif abs(left * 2 - s) == 1:
                    ans += 1
        return ans
