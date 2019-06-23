#include <iostream>

int get_change(int m) {
  //write your code here
  int coins_10 = m / 10;
  m = m % 10;
  int coins_5 = m / 5;
  m = m % 5;
  return m + coins_10 + coins_5;
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
