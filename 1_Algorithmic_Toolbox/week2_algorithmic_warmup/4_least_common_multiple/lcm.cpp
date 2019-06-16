#include <iostream>

using namespace std;

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

int gcd(int a, int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}

// a * b = LCM(a, b) * GCD(a, b)
// LCM(a, b) = (a * b) / GCD(a, b)
long long lcm_fast(int a, int b) {
  return ((long long) a * b) / gcd(a, b);
}

int main() {
  int a, b;
  std::cin >> a >> b;

  if (a < b) {
    int temp = a;
    a = b;
    b = temp;
  }
  std::cout << lcm_fast(a, b) << std::endl;
  return 0;
}
