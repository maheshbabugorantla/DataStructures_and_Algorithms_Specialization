#Uses python3

import sys
from math import log, ceil

def is_greater(digit, max_digit):
    return digit + max_digit > max_digit + digit

def greater_than_or_equal_to(number1, number2):

    if number2 == float('-Inf'):
        return True

    if number1 == 0:
        return True

    leading_digit_1 = 1 if number1 == 1 else number1 // (10 ** (ceil(log(number1, 10)) - 1))
    leading_digit_2 = 1 if number2 == 1 else number2 // (10 ** (ceil(log(number2, 10)) - 1))

    return leading_digit_1 >= leading_digit_2

def get_multiplier(digit):
    # if digit == 0:
    #     return 1
    if digit == 1:
        return 10
    else:
        return 10 ** ceil(log(digit, 10))

def largest_number(a):
    digits = list(map(int, a))
    answer = 0

    while digits:
        maxDigit = float('-Inf')
        for digit in digits:
            # print("Digit: {}, MaxDigit: {}".format(digit, maxDigit))
            if greater_than_or_equal_to(digit, maxDigit):
                maxDigit = digit
        answer = (answer * get_multiplier(maxDigit) + maxDigit)
        digits.remove(maxDigit)
    return answer

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
