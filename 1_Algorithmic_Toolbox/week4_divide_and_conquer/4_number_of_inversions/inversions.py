# Uses python3
import sys

def merge_sort(array):

    if len(array) == 1:
        return array, 0

    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    left, left_inversions = merge_sort(left)
    right, right_inversions = merge_sort(right)

    n_inversions = left_inversions + right_inversions

    # Merge Step

    i = 0
    j = 0

    merge_array = list()

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge_array.append(left[i])
            i += 1
        else:
            merge_array.append(right[j])
            j += 1
            n_inversions += (len(left) - i)

    while i < len(left):
        merge_array.append(left[i])
        i += 1

    while j < len(right):
        merge_array.append(right[j])
        j += 1

    return merge_array, n_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(merge_sort(a)[1])
