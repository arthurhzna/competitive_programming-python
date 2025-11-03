class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        i = 0
        n = len(colors)
        while i < n:
            j = i + 1
            s = neededTime[i]
            m = neededTime[i]
            while j < n and colors[j] == colors[i]:
                s += neededTime[j]
                if neededTime[j] > m:
                    m = neededTime[j]
                j += 1
            total += s - m
            i = j
        return total