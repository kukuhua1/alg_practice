from typing import List, Tuple
from collections import defaultdict, deque

class Solution:
    def max_count(self, wifi_routers: List[Tuple[int, int, int]]) -> int:
        n = len(wifi_routers)
        # 构建邻接表
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                dist = ((wifi_routers[i][0]-wifi_routers[j][0])**2 + 
                        (wifi_routers[i][1]-wifi_routers[j][1])**2) ** 0.5
                if wifi_routers[i][2] >= dist:
                    graph[i].append(j)
                if wifi_routers[j][2] >= dist:
                    graph[j].append(i)

        def reachable_count(start: int, u: int, v: int) -> int:
            visited = [False] * n
            queue = deque([start])
            visited[start] = True
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
                # 不直接改图，而是临时加上双向通路
                if node == u and not visited[v]:
                    visited[v] = True
                    queue.append(v)
                if node == v and not visited[u]:
                    visited[u] = True
                    queue.append(u)
            return sum(visited)

        max_size = 1
        for i in range(n):
            for j in range(i+1, n):
                for start in range(n):
                    max_size = max(max_size, reachable_count(start, i, j))

        return max_size

a = Solution()
wifi_routers = [[5, 6, 2], [7, 6, 1], [6, 5, 1], [4, 3, 2], [6, 3, 1], [7, 3, 1], [1, 5, 4], [2, 1, 3]]
print(a.max_count(wifi_routers))
