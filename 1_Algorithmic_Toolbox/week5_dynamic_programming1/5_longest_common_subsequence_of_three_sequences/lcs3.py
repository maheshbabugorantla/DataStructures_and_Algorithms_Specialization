#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    min_ed_distance = [[[0]*(len(a)+1) for i in range(len(b)+1)] for j in range(len(c)+1)]

    for i in range(1, len(c)+1):
        for j in range(1, len(b)+1):
            for k in range(1, len(a)+1):
                if (a[k-1] == b[j-1] and a[k-1] == c[i-1]):
                    min_ed_distance[i][j][k] = min_ed_distance[i-1][j-1][k-1] + 1
                else:
                    max_1 = max(min_ed_distance[i-1][j][k], min_ed_distance[i][j-1][k])
                    _max = max(max_1, min_ed_distance[i][j][k-1])
                    min_ed_distance[i][j][k] = _max

    return min_ed_distance[len(c)][len(b)][len(a)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
