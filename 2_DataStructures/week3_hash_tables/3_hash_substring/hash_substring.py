# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def poly_hash_function(s, p, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % p
    return ans


def pre_compute_hashes(T, P, p, x):
    """Pre Computes the Hashes
    Arguments:
        T {str} -- text
        P {str} -- pattern
        p {int} -- prime_number
        x {int} -- multiplier
    """
    len_T = len(T)
    len_P = len(P)

    hashes = [None] * (len_T - len_P + 1)
    S = T[len_T - len_P:]
    hashes[len_T - len_P] = poly_hash_function(S, p, x)
    y = 1
    for i in range(len_P):
        y = (y * x) % p
    for i in range(len_T - len_P - 1, -1, -1):
        hashes[i] = (x * hashes[i + 1] + ord(T[i]) - y * ord(T[i+len_P])) % p
    return hashes


def rabin_karp_algorithm(pattern, text):

    _multiplier = 263
    _prime = 1800000809
    # 1010364703
    # 1001037847
    # 1000001011
    # 1001037847

    hashes = pre_compute_hashes(text, pattern, _prime, _multiplier)
    pattern_hash = poly_hash_function(pattern, _prime, _multiplier)

    pattern_len = len(pattern)
    text_len = len(text)
    occurences = []

    for index in range(text_len - pattern_len + 1):
        _pattern = text[index:index+pattern_len]
        if (_pattern == pattern) and (hashes[index] == pattern_hash):
            occurences.append(index)
        index += 1

    return occurences


def get_occurrences(pattern, text):
    return rabin_karp_algorithm(pattern, text)


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
