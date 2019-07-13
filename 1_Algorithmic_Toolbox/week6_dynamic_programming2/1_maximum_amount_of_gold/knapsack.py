# Uses python3
import sys

def optimal_weight(W, w):
    if not W:
        return W

    ks_table = [[0 for _ in range(W+1)] for _ in range(len(w)+1)]

    for i in range(1, len(w) + 1):
        for weight in range(1, W + 1):
            ks_table[i][weight] = ks_table[i - 1][weight]
            if w[i-1] <= weight:
                ks_table[i][weight] = max(ks_table[i-1][weight-w[i-1]] + w[i-1], ks_table[i][weight])
    return ks_table[len(w)][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
