#include <iostream>
#include <cassert>
#include <vector>

using std::vector;

using namespace std;

int binary_search_helper(const vector<int> &a, int left, int right, int key) {

  if (left > right) {
    return -1;
  }

  int middle_index = (left + right) / 2;

  if (a[middle_index] == key) {
    return middle_index;
  } else if (a[middle_index] > key) {
    return binary_search_helper(a, left, middle_index-1, key);
  } else if (a[middle_index] < key) {
    return binary_search_helper(a, middle_index+1, right, key);
  }
  return -1;
}

int binary_search(const vector<int> &a, int x) {
  //write your code here
  return binary_search_helper(a, 0, (int)a.size()-1, x);
}

int linear_search(const vector<int> &a, int x) {
  for (size_t i = 0; i < a.size(); ++i) {
    if (a[i] == x) return i;
  }
  return -1;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  int m;
  std::cin >> m;
  vector<int> b(m);
  for (int i = 0; i < m; ++i) {
    std::cin >> b[i];
  }
  for (int i = 0; i < m; ++i) {
    //replace with the call to binary_search when implemented
    // std::cout << linear_search(a, b[i]) << ' ';
    std::cout << binary_search(a, b[i]) << ' ';
  }
}
