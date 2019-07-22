# python3

import sys
import threading

from collections import defaultdict

class TreeHeight:

    def __init__(self, nodes):
        self.nodes = nodes
        self.tree = defaultdict(list)
        self.tree_height = {key: 0 for key in range(len(nodes))}
        self._parse_tree()

    def _parse_tree(self):
        for i, node in enumerate(self.nodes):
            self.tree[node].append(i)

    def get_tree_max_height(self):
        root_node = -1

        # Search for root node
        for i, node in enumerate(self.nodes):
            # print(node)
            if node == -1:
                root_node = i
                break

        return self.get_tree_max_height_from_node(root_node)

    def get_tree_max_height_from_node(self, node):

        assert node >= 0 and node < len(self.nodes)

        if not self.tree[node]:
            return 1

        path_lengths = []

        for child in self.tree[node]:
            if self.tree_height[child]:
                path_lengths.append(self.tree_height[child])
            else:
                path_lengths.append(1 + self.get_tree_max_height_from_node(child))

        self.tree_height[node] = max(path_lengths)

        # print(self.tree_height)

        return self.tree_height[node]


def main():

    n = int(input())
    parents = list(map(int, input().split()))
    tree_height = TreeHeight(parents)
    print(tree_height.get_tree_max_height())

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
