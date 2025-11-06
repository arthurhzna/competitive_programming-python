class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa
        for u, v in connections:
            union(u, v)
        grid_members = defaultdict(list)
        for i in range(1, c + 1):
            grid_members[find(i)].append(i)
        grid_online = {root: SortedSet(members) for root, members in grid_members.items()}
        online = [True] * (c + 1)
        ans = []
        for t, x in queries:
            root = find(x)
            if t == 1:
                if online[x]:
                    ans.append(x)
                else:
                    ans.append(grid_online[root][0] if grid_online[root] else -1)
            else:
                if online[x]:
                    online[x] = False
                    grid_online[root].discard(x)
        return ans