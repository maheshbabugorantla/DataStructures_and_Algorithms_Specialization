#include <iostream>

int fibonacci_sum_squares_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current * current;
    }

    return sum % 10;
}

int fibonacci_sum_squares_fast(long long n) {

    // Summation of Squares of n Fibonacci Numbers
    // S(n) = FnFn+1
    // Proof
    // 1. https://www.youtube.com/watch?v=ruIwND9ytpE
    // 2. https://ima.org.uk/950/sum-of-the-squares-of-consecutive-fibonacci-numbers-puzzle/#

    if (n == 0 || n == 1) {
        return (int) (n * n);
    }

    if (n == 2) {
        return 2;
    }

    // S(n) = Fn+2 - 1
    // S(n-2) = Fn - 1
    // Fn = S(n-2) + 1
    // S(n) Sum of first n Fibonacci Numbers

    n = n % 60; // n = (n-2 + 2) % 60

    int prev = 0;
    int next = 1;

    int sum_n_2 = 0;

    for(int i = 2; i <= n; i++) {
        sum_n_2 = ((prev % 10) + (next % 10)) % 10;
        prev = next;
        next = sum_n_2;
    }

    if (sum_n_2 == 0) {
        sum_n_2 = 9;
    } else {
        sum_n_2 = (sum_n_2 % 10 - 1);
    }

    int f_n = (sum_n_2 + 1) % 10; // Fn = S(n-2) + 1
    int f_n1 = (f_n + prev) % 10; // Fn+1 = Fn + Fn-1

    // std::cout << "Fn = " << f_n << std::endl;
    // std::cout << "F_n1 = " << f_n1 << std::endl;

    return (f_n * f_n1) % 10;
}

int main() {
    long long n = 0;
    std::cin >> n;
    std::cout << fibonacci_sum_squares_fast(n) << std::endl;
}
