import math
from collections import deque


def bellman_ford_arbitrage_dynamic(weights, start, currencies):
    distances = dict()
    cycle = deque()

    for edge in weights.keys():
        distances.update({edge[0]: float('inf')})
        distances.update({edge[1]: float('inf')})

    distances.update({start: 0})
    cycle.append(start)

    for _ in range(1, len(currencies)):
        for edge in weights.keys():
            if distances[edge[1]] > distances[edge[0]] + weights.get(edge):
                distances.update({edge[1]: distances[edge[0]] + weights.get(edge)})
                cycle.append(edge[1])

    for edge in weights.keys():
        if distances[edge[1]] > distances[edge[0]] + weights.get(edge):
            return True, cycle

    return False, cycle


def main():
    num_currency_exchanges = int(input())
    currencies = set()
    currency_rates = dict()
    log_currency_rates = dict()

    start = [x for x in input().split(" ")]
    start_currency = start[0]
    currency_rates.update({(start[0], start[1]): float(start[2])})
    log_currency_rates.update({(start[0], start[1]): math.log(float(start[2]))})
    currencies.add(start[0])

    for _ in range(1, num_currency_exchanges):
        exchange = [x for x in input().split(" ")]
        currency_rates.update({(exchange[0], exchange[1]): float(exchange[2])})
        log_currency_rates.update({(exchange[0], exchange[1]): math.log(float(exchange[2]))})
        if exchange[0] not in currencies:
            currencies.add(exchange[0])

    found_cycle, path = \
        bellman_ford_arbitrage_dynamic(log_currency_rates, start_currency, currencies)

    if found_cycle:
        path.append(path[0])
        factor = 1.0
        path_string = ""
        for _ in range(len(path) - 1):
            path_string += path[_] + " => "
            if (path[_], path[_ + 1]) in currency_rates.keys():
                factor *= currency_rates.get((path[_], path[_ + 1]))

        if factor > 1.0:
            print("Arbitrage Detected")
            path_string += path[-1]
            print(path_string)
            factor = "{:.5f}".format(factor)
            print(factor + " factor increase ")
        else:
            print("No Arbitrage Detected")

    else:
        print("No Arbitrage Detected")


if __name__ == "__main__":
    main()