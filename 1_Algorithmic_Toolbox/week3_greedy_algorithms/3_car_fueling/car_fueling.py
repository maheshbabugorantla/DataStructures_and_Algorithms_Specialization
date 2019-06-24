# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    if (tank >= distance):
        return 0

    if (tank < stops[0]):
        return -1

    min_refills = 0
    prev_stop = 0

    gas_left_in_tank = tank

    for i in range(len(stops)):
        distance_covered = stops[i] - prev_stop
        gas_left_in_tank -= distance_covered

        # Ran out of the gas before reaching the next gas station
        if gas_left_in_tank < 0:
            return -1

        # Refill the gas if the car cannot reach the next gas station from the current
        if i < (len(stops) - 1) and (gas_left_in_tank < (stops[i+1] - stops[i])):
            gas_left_in_tank = tank # Refuel the tank
            min_refills += 1
        prev_stop = stops[i]

    # Checking if car needs to refuel at last gas station to reach destination
    if (gas_left_in_tank < (distance - stops[-1])):
        gas_left_in_tank = tank
        min_refills += 1
        gas_left_in_tank -= (distance - stops[-1])

    if gas_left_in_tank < 0:
        return -1

    return min_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
