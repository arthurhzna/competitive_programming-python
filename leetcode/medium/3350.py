class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        max_k = 0
        prev_len = 0  
        curr_len = 1 
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr_len += 1
            else:
                max_k = max(max_k, min(prev_len, curr_len))
                max_k = max(max_k, curr_len // 2)
                prev_len = curr_len
                curr_len = 1
        max_k = max(max_k, min(prev_len, curr_len))
        max_k = max(max_k, curr_len // 2)
        
        return max_k