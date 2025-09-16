class Solution:
    def jump(self, nums: List[int]) -> int:
        self.jumps = 0
        self.end = 0
        self.farthest = 0

        for i in range(len(nums) - 1):
            self.farthest = max(self.farthest, i + nums[i])
            if i == self.end:
                self.jumps += 1
                self.end = self.farthest

        return self.jumps
