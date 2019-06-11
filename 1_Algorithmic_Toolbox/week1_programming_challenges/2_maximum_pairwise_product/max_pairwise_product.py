# python3


def max_pairwise_product(numbers):

    # Finding the first two maximum numbers in the list of numbers
    max_number1 = float('-Inf')
    max_number2 = float('-Inf')

    for val in numbers:
        if val > max_number1:
            max_number2 = max_number1
            max_number1 = val
        elif val > max_number2:
            max_number2 = val

    return max_number1 * max_number2

def max_pairwise_product_slow(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
