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

int get_fibonacci_partial_sum_fast(long long from, long long to) {

    // If S(n) is the sum of fibonacci numbers from F0 to Fn
    // If S(m-1) is the sum of fibonacci numbers from F0 to Fm-1
    // Then, Fm + Fm+1 ... + Fn-1 + Fn = S(n) -  S(m-1)
    // S(n) = Fn+2 - 1
    // S(n) - S(m-1) = Fn+2 - Fm+1

    if (from == 0 && to == 0) {
        return 0;
    }

    // Fm+1 and Fn+2
    int F_m1 = 0;
    int F_n2 = 0;

    int prev = 0;
    int next = 1;

    for(int i = 2; i < from + 2; i++) {
        F_m1 = (prev % 10 + next % 10) % 10;
        prev = next;
        next = F_m1;
    }

    // cout << "Fm+1 = " << F_m1 << endl;

    for(int i = from + 2; i < to+3; i++) {
        F_n2 = (prev % 10 + next % 10) % 10;
        prev = next;
        next = F_n2;
    }

    // cout << "Fn+2 = " << F_n2 << endl;

    if (F_n2 < F_m1) {
        F_n2 = 10 + F_n2;
    }

    return (F_n2 - F_m1) % 10;
}

int main() {
    long long from, to;
    std::cin >> from >> to;
    std::cout << get_fibonacci_partial_sum_fast(from, to) << '\n';
}
