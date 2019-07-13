# Uses python3
import sys

def optimal_operations(n):

    min_operations = [0] * (n + 1)

    min_operation_sequence = []
    min_operation_sequence.append([0]) # 0
    min_operation_sequence.append([1]) # 1

    for val in range(2, n+1):
        min_op_3, min_op_2, min_op_1 = (float('Inf'),) * 3 # float('Inf'), float('Inf')

        if val % 3 == 0:
            min_op_3 = min_operations[val // 3] + 1
        elif val % 2 == 0:
            min_op_2 = min_operations[val // 2] + 1
        min_op_1 = min_operations[val - 1] + 1
        min_operations[val] = min(min_op_1, min_op_2, min_op_3)

        if min_operations[val] == min_op_3:
            min_operation_sequence.append(min_operation_sequence[val // 3] + [val])
        elif min_operations[val] == min_op_2:
            min_operation_sequence.append(min_operation_sequence[val // 2] + [val])
        else:
            min_operation_sequence.append(min_operation_sequence[val - 1] + [val])

    return min_operation_sequence[-1]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_operations(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
# optimal_operations = optimal_operations(n)
# print(optimal_operations)
