# Uses python3

import sys

from collections import deque

sys.setrecursionlimit(200000)

# node_id = 0

# Defunct Kosaraju SCC Method
# def kosaraju_dfs(adj, start_node, stack, on_stack, scc_count, ids, low):
#     stack.append(start_node)
#     on_stack[start_node] = True
#     global node_id
#     node_id += 1
#     ids[start_node], low[start_node] = node_id, node_id

#     for neighbor in adj[start_node]:
#         if ids[neighbor] == -1:
#             dfs(adj, neighbor, stack, on_stack, scc_count, ids, low)
#             low[start_node] = min(low[start_node], low[neighbor])
#         elif on_stack[neighbor]:
#             low[start_node] = min(low[start_node], ids[start_node])

#     if ids[start_node] == low[start_node]:
#         while stack:
#             node = stack.pop()
#             on_stack[node] = False
#             low[node] = ids[start_node]
#             if node == start_node:
#                 break
#         scc_count += 1
#     return scc_count


def reversed_graph(adj):
    reverse_adj = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for node in adj[i]:
            reverse_adj[node].append(i)
    return reverse_adj


def dfs(adj, x, visited, stack):

    visited[x] = True

    for neighbor in adj[x]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(adj, neighbor, visited, stack)
    stack.append(x)


def number_of_strongly_connected_components(adj):
    result = 0
    # write your code here
    n = len(adj)
    stack = deque()
    visited = [False for _ in range(n)]

    for node in range(n):
        if not visited[node]:
            dfs(adj, node, visited, stack)

    reverse_graph = reversed_graph(adj)
    visited = [False for _ in range(n)]

    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs(reverse_graph, node, visited, deque())
            result += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
