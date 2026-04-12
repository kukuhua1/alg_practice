import heapq
from collections import defaultdict

def best_path(connections, querys):
    graph = defaultdict(list)
    for conn in connections:
        src, dest, weight = conn
        graph[src].append((dest, weight))
        
    ans = [-1] * len(querys)

    for i, (src, dest) in enumerate(querys):
        best = defaultdict(lambda: (float('inf'), float('inf')))
        heap = [(0, 0, src)]
        best[src] = (0, 0)

        while heap:
            cur_links, cur_dist, node = heapq.heappop(heap)

            if (cur_links, cur_dist) > best[node]:
                continue

            if node == dest:
                ans[i] = cur_dist
                break
            
            for next_node, next_dist in graph[node]:
                new_links = cur_links + 1
                new_dist = cur_dist + next_dist
                if (new_links, new_dist) < best[next_node]:
                    best[next_node] = (new_links, new_dist)
                    heapq.heappush(heap, (new_links, new_dist, next_node))

    return ans 


connections = [[100, 101, 10], [102, 101, 5]]
querys = [[100, 101], [102, 100]]
print(best_path(connections, querys))
