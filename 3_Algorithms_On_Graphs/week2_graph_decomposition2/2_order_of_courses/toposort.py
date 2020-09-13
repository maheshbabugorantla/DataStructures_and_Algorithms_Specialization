#Uses python3

import sys
from collections import deque


def toposort(adj):
    neighbors = [0] * len(adj)
    order = []
    
    graph = [[] for _ in range(len(adj))]
    queue = deque()

    for course, pr in enumerate(adj):
        for n in pr:
            graph[n].append(course)
        neighbors[course] = len(pr)
        if neighbors[course] == 0:
            queue.append(course)

    completed_courses = set()
    while queue:
        course = queue.popleft()
        if course not in completed_courses:
            completed_courses.add(course)
            order.append(course)
            for neighbor in graph[course]:
                neighbors[neighbor] -= 1
                if neighbors[neighbor] == 0:
                    queue.append(neighbor)
    return order[::-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
