#Uses python3

import sys

def lcs2(a, b):

    min_ed = [[0] * (len(a)+1) for _ in range(len(b)+1)]

    for row in range(1, len(b)+1):
        for col in range(1, len(a)+1):
            if a[col - 1] == b[row - 1]:
                min_ed[row][col] = min_ed[row - 1][col - 1] + 1
            else:
                min_ed[row][col] = max(min_ed[row][col-1], min_ed[row-1][col])
    return min_ed[len(b)][len(a)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
