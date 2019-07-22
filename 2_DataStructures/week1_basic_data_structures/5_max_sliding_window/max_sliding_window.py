# python3

from collections import deque

def max_sliding_window_eff(sequence, m):

    queue = deque()

    maximums = list()

    # Maximum from first sliding window
    for i in range(m):
        while queue and sequence[queue[-1]] < sequence[i]:
            queue.pop()
        queue.append(i)

    maximums.append(sequence[queue[0]])

    for i in range(m, len(sequence)):

        # Removing the elements that are out of the sliding window
        while queue and queue[0] <= i - m:
            queue.popleft()

        # Removing the elements that are less than the current element
        while queue and sequence[queue[-1]] < sequence[i]:
            queue.pop()

        queue.append(i)
        maximums.append(sequence[queue[0]])

    return maximums

# Flunks on the bigger size sequence such as above 1000 and sliding window sizes
def _max_sliding_window_efficient(sequence, m):

    queue = sequence[:m]
    maximums = [max(queue)]
    rolling_index = 0

    i = m

    while i < len(sequence):
        queue[rolling_index] = sequence[i]
        maximums.append(max(queue))
        rolling_index = (rolling_index + 1) % m
        i += 1
    return maximums


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    # import timeit
    # start_timer = timeit.default_timer()
    print(" ".join(map(str, max_sliding_window_eff(input_sequence, window_size))))
    # print(timeit.default_timer() - start_timer)

    # input_sequence = [0 for _ in range(100000)]
    # window_size = 33333
    # import timeit
    # start_timer = timeit.default_timer()
    # maximums = max_sliding_window_eff(input_sequence, window_size)
    # print("{} seconds".format(timeit.default_timer() - start_timer))
    # print(len(maximums))
