# Uses python3
import sys

def gen_bag_items(weights, values):
    return [(weight, value, (value / weight)) for weight, value in zip(weights, values)]

def get_optimal_value(capacity, weights, values):
    max_loot_value = 0.

    bag_items = gen_bag_items(weights, values)
    bag_items.sort(key=lambda item: item[2])

    while capacity > 0 and len(bag_items):
        bag_item = bag_items.pop()
        weight = min(bag_item[0], capacity)
        max_loot_value += weight * bag_item[2]
        capacity -= weight
    return max_loot_value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
