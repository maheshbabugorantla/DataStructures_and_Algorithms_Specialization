#include <iostream>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

using std::vector;

bool sort_desc(const tuple<double, int>& a, const tuple<double, int>& b) {
  return (get<0>(a) > get<0>(b));
}

double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {

  vector<tuple<double, int>> value_per_unit;

  for (unsigned int i = 0; i < values.size(); i++) {
    value_per_unit.push_back(make_tuple((double) values[i] / weights[i], i));
  }

  sort(value_per_unit.begin(), value_per_unit.end(), sort_desc);

  // for(unsigned int i = 0; i < value_per_unit.size(); i++) {
  //   cout << get<0>(value_per_unit[i]) << ' ';
  //   cout << get<1>(value_per_unit[i]) << endl;
  // }
  // cout << endl;

  double max_value_of_loot = 0.0;

  int a = 0;

  // write your code here
  for(unsigned int i = 0; i < value_per_unit.size(); i++) {
    if (capacity == 0) {
      return max_value_of_loot;
    }

    if (weights[i] < capacity) {
      a = weights[get<1>(value_per_unit[i])];
    } else {
      a = capacity;
    }

    max_value_of_loot += (a * get<0>(value_per_unit[i]));
    capacity -= a;
  }

  return max_value_of_loot;
}

int main() {
  int n;
  int capacity;
  cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values);

  cout.precision(10);
  cout << optimal_value << endl;
  return 0;
}
