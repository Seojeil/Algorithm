import sys

_ = sys.stdin.readline()

road = list(map(int, sys.stdin.readline().split()))


def uphill(road):
    start = road[0]
    result = 0

    for i, r in enumerate(road[1:]):
        if road[i] >= r:
            result = max(result, road[i] - start)
            start = r
    else:
        result = max(result, road[-1] - start)

    return result


print(uphill(road))