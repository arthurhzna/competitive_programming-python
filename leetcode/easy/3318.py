class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            sub = nums[i:i+k]
            c = Counter(sub)
            s = sorted(c.items(), key=lambda a: (a[1], a[0]), reverse=True)
            top = [num for num, _ in s[:x]]
            ans.append(sum(num for num in sub if num in top))
        return ans
