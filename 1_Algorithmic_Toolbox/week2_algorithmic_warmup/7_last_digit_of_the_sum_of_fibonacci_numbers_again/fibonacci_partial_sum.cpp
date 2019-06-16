#include <iostream>
#include <vector>

using namespace std;
using std::vector;

long long get_fibonacci_partial_sum_naive(long long from, long long to) {
    long long sum = 0;

    long long current = 0;
    long long next  = 1;

    for (long long i = 0; i <= to; ++i) {
        if (i >= from) {
            sum += current;
        }

        long long new_current = next;
        next = next + current;
        current = new_current;
    }

    return sum % 10;
}

int get_last_digit_of_fibonacci_sum(long long n) {

    int prev = 0;
    int next = 1;

    n = (n + 2) % 60;

    int fibo_number = 1;

    for(int i = 2; i <= n; i++) {
        fibo_number = (prev % 10 + next % 10) % 10;
        prev = next;
        next = fibo_number;
    }

    if (fibo_number == 0) {
        return 9;
    }

    return (fibo_number % 10) - 1;
}

int get_fibonacci_partial_sum_fast(long long from, long long to) {

    // If S(n) is the sum of fibonacci numbers from F0 to Fn
    // If S(m-1) is the sum of fibonacci numbers from F0 to Fm-1
    // Then, Fm + Fm+1 ... + Fn-1 + Fn = S(n) -  S(m-1)
    // S(n) = Fn+2 - 1
    // S(n) - S(m-1) = Fn+2 - Fm+1

    int last_digit_to = get_last_digit_of_fibonacci_sum(to);
    int last_digit_from = get_last_digit_of_fibonacci_sum(from - 1);

    // cout << "Last Digit of From: " << last_digit_from << endl;
    // cout << "Last Digit of To: " << last_digit_to << endl;

    return (last_digit_to > last_digit_from) ? (last_digit_to - last_digit_from) % 10 : ((last_digit_to + 10) - last_digit_from) % 10;
}

int main() {
    long long from, to;
    std::cin >> from >> to;
    std::cout << get_fibonacci_partial_sum_fast(from, to) << '\n';
}
