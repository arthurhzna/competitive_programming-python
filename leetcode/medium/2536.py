class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        for i in range(n):
            row = diff[i]
            for j in range(n):
                row[j + 1] += row[j]

        for j in range(n):
            col_j = diff
            for i in range(n):
                col_j[i + 1][j] += col_j[i][j]

        res = diff
        return [res[i][:n] for i in range(n)]
