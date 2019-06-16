#include <iostream>

using namespace std;

long long get_fibonacci_huge_naive(long long n, long long m) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % m;
}

// For any integer m ≥ 2,
// the sequence Fn mod m is periodic.
// The period always starts with 01
// and is known as Pisano period
long long calculate_pisano_period_length(long long m) {
    long long first = 0, second = 1, third = first + second;

    for(long long i = 0; i < (m * m); i++) {
        third = (first + second) % m;
        first = second;
        second = third;
        if (first == 0 && second == 1) return i + 1;
    }
    return 2;
}

long long fibonacci_n_modulo_m(long long n, long m) {
    if (n <= 1) {
        return n;
    }

    if (n == 2) {
        return 1;
    }

    long long prev = 0;
    long long next = 1;

    long long fibonacci_number = (prev + next) % m;

    for (long long i = 2; i < n; i++) {
        prev = next;
        next = fibonacci_number;
        fibonacci_number = (prev + next) % m;
    }

    return fibonacci_number % m;
}

long long get_fibonacci_huge_fast(long long n, long long m) {
    long long pisano_period_length = calculate_pisano_period_length(m);
    return fibonacci_n_modulo_m(n % pisano_period_length, m);
}

int main() {
    long long n, m;
    cin >> n >> m;
    cout << get_fibonacci_huge_fast(n, m) << '\n';
}
