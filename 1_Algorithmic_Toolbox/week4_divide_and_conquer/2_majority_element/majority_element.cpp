#include <algorithm>
#include <iostream>
#include <vector>

using std::vector;

int boyer_moore_majority_element(vector<int> &a, int size) {
  int majority_element = -1;

  int counter = 0;

  for(int j = 0; j < size; j++) {

    if(counter == 0) {
      majority_element = a[j];
      counter = 1;
    } else if (a[j] == majority_element) {
      counter += 1;
    } else {
      counter -= 1;
    }
  }

  counter = 0;

  // Second Linear Pass to confirm the Majority
  for(int i = 0; i < size; i++) {
    if (majority_element == a[i]) {
      counter += 1;
    }
  }

  return (counter > (size/2)) ? majority_element : -1;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  std::cout << (boyer_moore_majority_element(a, (int)a.size()) != -1) << '\n';
}
