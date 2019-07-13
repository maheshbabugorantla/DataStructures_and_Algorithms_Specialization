# Uses python3
def edit_distance(s, t):
    min_ed_matrix = [[0]*(len(s) + 1) for val in range(len(t)+1)]
    min_ed_matrix[0] = [val for val in range(len(s)+1)]

    for val in range(1, len(t)+1):
        min_ed_matrix[val][0] = val

    for row in range(1, len(t) + 1):
        for col in range(1, len(s) + 1):
            insertion = min_ed_matrix[row][col-1]+1
            deletion = min_ed_matrix[row-1][col]+1
            match = min_ed_matrix[row-1][col-1]
            mismatch = min_ed_matrix[row-1][col-1] + 1

            if t[row-1] == s[col-1]:
                min_ed_matrix[row][col] = min(insertion, deletion, match)
            else:
                min_ed_matrix[row][col] = min(insertion, deletion, mismatch)

    return min_ed_matrix[len(t)][len(s)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
