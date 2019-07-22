# python3

from collections import namedtuple


class Stack(object):

    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):

    Bracket = namedtuple("Bracket", ["char", "position"])

    opening_brackets_stack = Stack()

    for i, next in enumerate(text):
        if next in "([{":
            bracket = Bracket(next, position=i+1)
            opening_brackets_stack.push(bracket)

        if next in ")]}":
            _bracket = opening_brackets_stack.peek()
            if not _bracket or not are_matching(_bracket.char, next):
                return i + 1
            opening_brackets_stack.pop()
    left_bracket = opening_brackets_stack.peek()
    return -1 if not left_bracket else left_bracket.position


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print("Success" if mismatch == -1 else mismatch)


if __name__ == "__main__":
    main()
