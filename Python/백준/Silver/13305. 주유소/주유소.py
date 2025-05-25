N = int(input())
roads = list(map(int, input().split()))
citys = list(map(int, input().split()))

road = 0
cur_city = float('inf')
result = 0

while roads:
    road += roads.pop(0)
    cur_city = min(cur_city, citys.pop(0))

    next_city = citys[0]

    if cur_city > next_city:
        result += cur_city * road

        road = 0

result += cur_city * road

print(result)