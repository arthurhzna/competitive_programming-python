from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        # Precompute the length of strictly increasing subarray starting at each index
        inc_length = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc_length[i] = inc_length[i + 1] + 1
        
        # Check if there exist two adjacent subarrays of length k that are strictly increasing
        for i in range(n - 2 * k + 1):
            if inc_length[i] >= k and inc_length[i + k] >= k:
                return True
        
        return False