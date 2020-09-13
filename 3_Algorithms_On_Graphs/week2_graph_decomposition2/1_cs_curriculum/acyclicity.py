#Uses python3

import sys

from collections import deque

def acyclic(adj):

    for node in range(len(adj)):
        queue = deque([node])
        visited_nodes = set()
        while queue:
            _node = queue.popleft()
            if _node in visited_nodes and _node == node:
                return 1
            if _node not in visited_nodes:
                visited_nodes.add(_node)
                for neighbor in adj[_node]:
                    queue.append(neighbor)
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
