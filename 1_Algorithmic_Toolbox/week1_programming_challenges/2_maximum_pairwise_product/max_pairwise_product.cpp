#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long MaxPairwiseProduct(const vector<int> & numbers) {

    int size = numbers.size();

    int maxIndex1 = 0;
    int maxIndex2 = size - 1;

    for(int i = 1; i < size; i++) {
        if (numbers[i] > numbers[maxIndex1]) {
            maxIndex2 = maxIndex1;
            maxIndex1 = i;
        } else if (numbers[maxIndex2] < numbers[i]){
            maxIndex2 = i;
        }
    }

    // cout << numbers[maxIndex1] << endl;
    // cout << numbers[maxIndex2] << endl;

    return (long long) numbers[maxIndex1] * numbers[maxIndex2];
}

// int MaxPairwiseProduct_Slow(const std::vector<int>& numbers) {
//     int max_product = 0;
//     int n = numbers.size();

//     for (int first = 0; first < n; ++first) {
//         for (int second = first + 1; second < n; ++second) {
//             max_product = std::max(max_product,
//                 numbers[first] * numbers[second]);
//         }
//     }

//     return max_product;
// }

int main() {
    int n;
    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProduct(numbers) << "\n";
    return 0;
}
