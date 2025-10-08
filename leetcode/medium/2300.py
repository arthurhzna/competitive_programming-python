class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        res = []

        for s in spells:
            min_potion = (success + s - 1) // s  
            idx = bisect_left(potions, min_potion)
            res.append(n - idx)

        return res #
