# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c


  def _inOrder(self, root):
      if root == -1:
        return
      self._inOrder(self.left[root])
      self.result.append(self.key[root])
      self._inOrder(self.right[root])


  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._inOrder(0)
    # print("In Order: {}".format(self.result))
    return " ".join(map(str, self.result))


  def _preOrder(self, root):
    if root == -1:
      return
    self.result.append(self.key[root])
    self._preOrder(self.left[root])
    self._preOrder(self.right[root])

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._preOrder(0)
    # print("Pre Order: {}".format(self.result))
    return " ".join(map(str, self.result))

  def _postOrder(self, root):
    if root == -1:
      return
    self._postOrder(self.left[root])
    self._postOrder(self.right[root])
    self.result.append(self.key[root])

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._postOrder(0)
    # print("Post Order: {}".format(self.result))
    return " ".join(map(str, self.result))


def main():
	tree = TreeOrders()
	tree.read()
	print(tree.inOrder())
	print(tree.preOrder())
	print(tree.postOrder())

threading.Thread(target=main).start()
