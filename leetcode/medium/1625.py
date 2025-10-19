class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        res = s
        n = len(s)

        def add_op(x):
            x = list(x)
            for i in range(1, n, 2):
                x[i] = str((int(x[i]) + a) % 10)
            return "".join(x)

        def rotate_op(x):
            return x[-b:] + x[:-b]

        def dfs(cur):
            nonlocal res
            if cur in visited:
                return
            visited.add(cur)
            if cur < res:
                res = cur
            dfs(add_op(cur))
            dfs(rotate_op(cur))

        dfs(s)
        return res
