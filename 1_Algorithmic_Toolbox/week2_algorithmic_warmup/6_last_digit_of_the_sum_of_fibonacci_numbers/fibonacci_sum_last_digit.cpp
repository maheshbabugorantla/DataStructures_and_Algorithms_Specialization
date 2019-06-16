#include <iostream>

using namespace std;

int fibonacci_sum_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current;
    }

    return sum % 10;
}

int get_pisano_period_length(int n) {
    long long first = 0, second = 1, third = first + second;

    for(long long i = 0; i < n * n; i++) {
        third = (first + second) % n;
        first = second;
        second = third;
        if(first == 0 && second == 1) return i + 1;
    }
    return 2;
}

int fibonacci_sum_last_digit_fast(long long n) {

    if (n <= 1) {
        return n;
    }

    if (n == 2) {
        return 2;
    }

    // int pisano_period_10 = get_pisano_period_length(10);
    // pisano_period_10 is 60

    // Fn = Fn-1 + Fn-2
    // Fn+1 = Fn + Fn-1
    // Fn+1 will gives us the summation of `n` fibonacci numbers
    // Hence we need to compute (n + 2) fibonacci numbers
    // Because pisano period length of 10 is 60.
    // Therefore, the number of fibonacci numbers we need to compute will always be less than 63
    n = (n + 2) % 60;

    int prev = 0;
    int next = 1;

    int fib_number = 1;

    for(long long i = 2; i <= n; i++) {
        fib_number = (prev % 10 + next % 10) % 10;
        prev = next;
        next = fib_number;
    }

    if (fib_number == 0) {
        return 9;
    }

    return fib_number % 10 - 1;
}

int main() {
    long long n = 0;
    std::cin >> n;
    cout << fibonacci_sum_last_digit_fast(n) << endl;
}

// 832564823476
