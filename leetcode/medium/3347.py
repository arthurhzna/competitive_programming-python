class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        import collections
        from sortedcontainers import SortedDict

        res = 1
        running = 0
        freq = collections.Counter(nums)
        sweep = SortedDict()
        pts = set()

        for x in nums:
            sweep[x - k] = sweep.get(x - k, 0) + 1
            sweep[x + k + 1] = sweep.get(x + k + 1, 0) - 1
            pts.add(x)
            pts.add(x - k)
            pts.add(x + k + 1)

        for x in sorted(pts):
            running += sweep.get(x, 0)
            changable = running - freq[x]
            res = max(res, freq[x] + min(numOperations, changable))

        return res
