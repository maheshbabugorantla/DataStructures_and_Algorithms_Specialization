#Uses python3

import sys
from collections import deque


def bipartite(adj):
    #write your code here
    n = len(adj)
    color_map = [-1] * n

    for i in range(n):
        if color_map[i] == -1:
            queue = deque([i])
            color_map[i] = 1
            while queue:
                node = queue.popleft()
                nc = 1 - color_map[node]
                for neighbor in adj[node]:
                    if color_map[neighbor] == color_map[node]:
                        return 0
                    if color_map[neighbor] == -1:
                        queue.append(neighbor)
                        color_map[neighbor] = nc
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
