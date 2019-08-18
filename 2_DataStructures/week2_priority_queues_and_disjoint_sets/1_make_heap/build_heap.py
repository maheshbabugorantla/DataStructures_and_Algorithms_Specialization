# python3


def parent(i):
    assert isinstance(i, int)
    return (i - 1)//2


def left_child(i):
    assert isinstance(i, int)
    return 2*i + 1


def right_child(i):
    assert isinstance(i, int)
    return 2*i + 2


def sift_down_swaps(data, i, swaps):
    min_index = i

    size = len(data)

    l_child = left_child(i)

    if l_child < size and data[l_child] < data[min_index]:
        min_index = l_child

    r_child = right_child(i)

    if r_child < size and data[r_child] < data[min_index]:
        min_index = r_child

    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        swaps = sift_down_swaps(data, min_index, swaps)
    return swaps


def min_heap_swaps(data):

    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):
        swaps = sift_down_swaps(data, i, swaps)
    return swaps


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = min_heap_swaps(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
