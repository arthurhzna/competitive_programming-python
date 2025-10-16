from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counts = [0] * value
        for num in nums:
            counts[num % value] += 1

        full_cycles = min(counts)
        for remainder in range(value):
            if counts[remainder] == full_cycles:
                return full_cycles * value + remainder