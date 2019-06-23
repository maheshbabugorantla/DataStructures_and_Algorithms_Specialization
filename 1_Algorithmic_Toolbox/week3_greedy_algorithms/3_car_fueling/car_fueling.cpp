#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;
using std::max;

int compute_min_refills(int dist, int tank, vector<int> & stops) {
    // write your code here

    if (tank >= dist) {
        return 0;
    }

    if (tank < stops[0]) {
        return -1;
    }

    int min_refills = 0;
    int prev_stop = 0;

    int gas_left_in_the_tank = tank;

    for(unsigned int i = 0; i < stops.size(); i++) {
        // cout << "Current Stop: " << stops[i] << std::endl;
        int distance_covered = stops[i] - prev_stop;
        gas_left_in_the_tank -= distance_covered;

        if (gas_left_in_the_tank < 0) {
            return -1;
        }

        if (gas_left_in_the_tank < (stops[i + 1] - stops[i])) {
            // cout << "Refuelling" << std::endl;
            min_refills += 1;
            gas_left_in_the_tank = tank; // Refuel
        }
        prev_stop = stops[i];
    }

    // Covering the left over distance to the destination from the final gas stop
    if (gas_left_in_the_tank < (dist - stops[stops.size() - 1])) {
        // cout << "Refuelling at the final gas stop" << std::endl;
        min_refills += 1;
        gas_left_in_the_tank = tank; // Refuel at the final stop
        gas_left_in_the_tank -= (dist - stops[stops.size() - 1]);
    }

    if (gas_left_in_the_tank < 0) {
        return -1;
    }

    return min_refills;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n);
    for (int i = 0; i < n; ++i)
        cin >> stops.at(i);

    cout << compute_min_refills(d, m, stops) << "\n";

    return 0;
}
