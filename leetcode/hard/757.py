class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        a, b = -1, -1
        res = 0

        for s, e in intervals:
            if s > b:
                res += 2
                b = e
                a = e - 1
            elif s > a:
                res += 1
                a = b
                b = e

        return res
