#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def is_bst(tree, root, min_val, max_val):
  if len(tree) < 2:
    return True

  if root == -1:
    return True
  if tree[root][0] < min_val or tree[root][0] > max_val:
    return False
  return is_bst(tree, tree[root][1], min_val, tree[root][0]-1) and is_bst(tree, tree[root][2], tree[root][0], max_val)


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  keys = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if is_bst(tree, 0, float('-Inf'), float('Inf')):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
