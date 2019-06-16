#include <iostream>

int get_fibonacci_last_digit_fast(int n) {
    if (n <= 1) {
        return n;
    }

    int previous = 0;
    int next = 1;

    int fibo_last_digit = (previous + next) % 10;

    for (int i = 2; i < n; i++) {
        previous = next;
        next = fibo_last_digit;
        fibo_last_digit = (previous + next) % 10;
    }
    return fibo_last_digit;
}

int get_fibonacci_last_digit_naive(int n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;

    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % 10;
}

int main() {
    int n;
    std::cin >> n;
    int c = get_fibonacci_last_digit_fast(n);
    std::cout << c << '\n';
}
