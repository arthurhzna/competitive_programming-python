class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        num_count = defaultdict(int)
        sweep = defaultdict(int)
      
        for number in nums:
            num_count[number] += 1
            sweep[number] += 0
            sweep[number - k] += 1
            sweep[number + k + 1] -= 1
      
        max_freq = 0
        running_sum = 0
      
        for position, delta in sorted(sweep.items()):
            running_sum += delta
            max_freq = max(max_freq, min(running_sum, num_count[position] + numOperations))
      
        return max_freq