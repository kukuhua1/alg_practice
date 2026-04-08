import heapq
from collections import defaultdict


def min_router_delay(router_num, link_relations, router_ri, router_rj):
    if router_ri == router_rj:
        return 0
    
    graph = defaultdict(list)
    for link in link_relations:
        graph[link[0]].append((link[1], link[2]))
        graph[link[1]].append((link[0], link[2]))

    dists = [float("inf")] * (router_num + 1)
    dists[router_ri] = 0

    heap = [(0, router_ri)]

    while heap:
        cur_dist, node = heapq.heappop(heap)

        if cur_dist > dists[node]:
            continue # 更新了某个节点的最短距离，但是旧的状态还在堆里，此时旧的状态不跳过，将会重复搜索，所以直接跳过

        if node == router_rj:
            return cur_dist

        for cur_node, dist in graph[node]:
            new_dist = cur_dist + dist
            if new_dist < dists[cur_node]:
                dists[cur_node] = new_dist
                heapq.heappush(heap, (new_dist, cur_node))
    return -1


        

router_num = 4
link_relations = [
    [1, 2, 10],
    [1, 3, 1],
    [3, 2, 1],
    [2, 4, 8]
]
router_ri = 1
router_rj = 4

print(min_router_delay(router_num, link_relations, router_ri, router_rj))