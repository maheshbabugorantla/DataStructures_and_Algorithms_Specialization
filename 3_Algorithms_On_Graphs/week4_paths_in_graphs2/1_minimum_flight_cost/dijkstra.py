# Uses python3

import sys
from heapq import heappop, heappush


class Vertex:

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f"{self.vertex}: {self.weight}"


def distance(adj, cost, s, t):

    if not adj:
        return float('Inf')

    n = len(adj)
    s_dist = [float('Inf') for _ in range(n)]
    # prev = [None for _ in range(n)]
    s_dist[s] = 0

    # Build Explore List with Associated Weights
    explore_list = []
    for i, edge in enumerate(adj[s]):
        heappush(explore_list, Vertex(edge, cost[s][i]))
        s_dist[edge] = cost[s][i]
        # prev[edge] = s

    # Explore the Shortest Distance from s to t
    while explore_list:
        vertex = heappop(explore_list)
        node = vertex.vertex
        for neighbor, weight in zip(adj[node], cost[node]):
            if s_dist[neighbor] > s_dist[node] + weight:
                s_dist[neighbor] = s_dist[node] + weight
                # prev[neighbor] = node
                heappush(explore_list, Vertex(neighbor, s_dist[neighbor]))

    return s_dist[t] if s_dist[t] != float('Inf') else -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
