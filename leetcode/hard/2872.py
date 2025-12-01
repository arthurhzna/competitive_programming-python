class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        ans = 0
        visited = [False] * n

        def dfs(u):
            nonlocal ans
            visited[u] = True
            s = values[u]
            for v in g[u]:
                if not visited[v]:
                    s += dfs(v)
            if s % k == 0:
                ans += 1
                return 0
            return s

        dfs(0)
        return ans