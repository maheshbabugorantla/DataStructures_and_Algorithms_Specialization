# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    digits = list(map(int, dataset[::2]))
    ops = dataset[1::2]

    from copy import deepcopy

    max_val_matrix = [[0 for _ in digits] for _ in digits]
    min_val_matrix = deepcopy(max_val_matrix)

    for i, digit in enumerate(digits):
        max_val_matrix[i][i], min_val_matrix[i][i] = digit, digit

    for i in range(len(digits)):
        for j in range(0, len(digits)-i-1):
            k = i + j + 1
            min_value = float('Inf')
            max_value = float('-Inf')
            for l in range(j, k):
                a = evalt(max_val_matrix[j][l], max_val_matrix[l + 1][k], ops[l])
                b = evalt(max_val_matrix[j][l], min_val_matrix[l + 1][k], ops[l])
                c = evalt(min_val_matrix[j][l], max_val_matrix[l + 1][k], ops[l])
                d = evalt(min_val_matrix[j][l], min_val_matrix[l + 1][k], ops[l])
                min_value = min(min_value, a, b, c, d)
                max_value = max(max_value, a, b, c, d)
            max_val_matrix[j][k] = max_value
            min_val_matrix[j][k] = min_value

    return max_val_matrix[0][len(digits) - 1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
