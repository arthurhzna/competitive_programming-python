class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7
        remaining_days = n % 7
        total = 0
        for i in range(full_weeks):
            total += 28 + i * 7
        start = full_weeks + 1
        for j in range(remaining_days):
            total += start + j
        return total
