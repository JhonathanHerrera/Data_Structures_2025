import heapq
from collections import defaultdict
from typing import List, Tuple

class Solution:
    def dijkstra(self, n: int, edges: List[Tuple[int, int, int]], start: int) -> List[int]:
        """
        :param n: number of nodes (0-indexed: 0...n-1)
        :param edges: list of (u, v, w) meaning edge u->v with weight w
        :param start: starting node
        :return: shortest distance from start to all nodes
        """

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [float("inf")] * n
        dist[start] = 0

        heap = [(0, start)]

        while heap:
            cost, node = heapq.heappop(heap)

            if cost > dist[node]:
                continue

            for nei, w in graph[node]:
                new_cost = cost + w
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    heapq.heappush(heap, (new_cost, nei))

        return dist
