from typing import List

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if not nums:  
#             return 0
#         i = 0  
#         for j in range(1, len(nums)):
#             if nums[j] != nums[i]:  
#                 i += 1
#                 nums[i] = nums[j]
#         return i + 1 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        write = 1  
        prev = nums[0]
        for j in range(1, n):
            curr = nums[j]
            if curr != prev:         
                nums[write] = curr
                write += 1
                prev = curr          
        return write




