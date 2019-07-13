# Uses python3
import sys

def get_change(money, coins):

    if not isinstance(money, int):
        raise TypeError("money should be an 'int'")

    if not money:
        return 0

    min_coins = [float('Inf')] * (money + 1)

    min_coins[0] = 0

    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                min_coins[m] = min(min_coins[m-coin] + 1, min_coins[m])
            else:
                break
    return min_coins[-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m, [1, 3, 4]))
