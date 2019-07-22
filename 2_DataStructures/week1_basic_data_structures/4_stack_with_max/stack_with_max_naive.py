# python3

import sys

class Stack(object):

    def __init__(self, datatype=None):
        self.datatype = datatype
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, element):
        if not isinstance(element, self.datatype):
            raise TypeError("'element' should be of {}".format(self.datatype))
        self.stack.append(element)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]


class Item:
    def __init__(self, value):
        self.value = value


class MaxStack:

    def __init__(self, datatype=None):
        self.stack = Stack(datatype)

    def push(self, item):
        if len(self.stack) == 0:
            self.stack.push([item, item])
        else:
            self.stack.push([item, max(item, self.peek()[1])])

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def getMax(self):
        return self.peek()[1]

def main():
    stack = MaxStack(datatype=list)
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.getMax())
        else:
            assert(0)


if __name__ == "__main__":
    main()
