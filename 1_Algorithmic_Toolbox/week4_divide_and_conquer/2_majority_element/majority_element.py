# Uses python3
import sys


def get_majority_element(a, left, right):

    map = dict()

    for val in a:
        if not map.get(val, None):
            map[val] = 1
        else:
            map[val] += 1
            if map[val] > len(a) // 2:
                return map[val]
    return -1


# def get_majority_element(a, left, right):
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#     #write your code here
#     return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
