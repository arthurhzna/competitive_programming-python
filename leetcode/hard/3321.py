from collections import Counter
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def add_item(v: int):
            if freq[v] == 0:
                return
            t = (freq[v], v)
            if main_set and t > main_set[0]:
                nonlocal total
                total += t[0] * t[1]
                main_set.add(t)
            else:
                aux_set.add(t)

        def remove_item(v: int):
            if freq[v] == 0:
                return
            t = (freq[v], v)
            if t in main_set:
                nonlocal total
                total -= t[0] * t[1]
                main_set.remove(t)
            else:
                aux_set.remove(t)

        main_set = SortedList()
        aux_set = SortedList()
        freq = Counter()
        total = 0
        n = len(nums)
        out = [0] * (n - k + 1)

        for i, v in enumerate(nums):
            remove_item(v)
            freq[v] += 1
            add_item(v)

            start = i - k + 1
            if start < 0:
                continue

            while aux_set and len(main_set) < x:
                f, val = aux_set.pop()
                main_set.add((f, val))
                total += f * val

            while len(main_set) > x:
                f, val = main_set.pop(0)
                total -= f * val
                aux_set.add((f, val))

            out[start] = total

            rem = nums[start]
            remove_item(rem)
            freq[rem] -= 1
            if freq[rem] > 0:
                add_item(rem)

        return out
