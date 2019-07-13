# Uses python3
import sys


def binary_search_helper(a, left, right, x):
    if left >= right:
        return -1

    # write your code here
    middle_index = (left + right) // 2

    if (a[middle_index] == x):
        return middle_index
    elif (a[middle_index] > x):
        return binary_search_helper(a, left, middle_index, x)
    elif (a[middle_index] < x):
        return binary_search_helper(a, middle_index+1, right, x)
    return -1


def binary_search(a, x):
    return binary_search_helper(a, 0, len(a)-1, x)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end=' ')


if __name__ == '__main__':
    main()
