class Solution:
    def maxPower(self, s: list[int], r: int, k: int) -> int:
        def ok(x: int, left: int) -> bool:
            diff = [0] * (n + 1)
            cur = 0
            for i in range(n):
                cur += diff[i]
                need = x - (base[i] + cur)
                if need > 0:
                    if left < need:
                        return False
                    left -= need
                    pos = min(i + r, n - 1)
                    l = max(0, pos - r)
                    rr = min(pos + r, n - 1)
                    diff[l] += need
                    diff[rr + 1] -= need
                    cur += need
            return True

        n = len(s)
        diff = [0] * (n + 1)
        for i, val in enumerate(s):
            l = max(0, i - r)
            rr = min(i + r, n - 1)
            diff[l] += val
            diff[rr + 1] -= val
        base = list(accumulate(diff))

        lo, hi = 0, 1 << 40
        while lo < hi:
            mid = (lo + hi + 1) >> 1
            if ok(mid, k):
                lo = mid
            else:
                hi = mid - 1
        return lo