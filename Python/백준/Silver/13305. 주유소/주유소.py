from collections import deque


N = int(input())
roads = deque(map(int, input().split()))
citys = deque(map(int, input().split()))

road = 0
cur_city = float('inf')
result = 0

while roads:
    road += roads.popleft()
    cur_city = min(cur_city, citys.popleft())

    next_city = citys[0]

    if cur_city > next_city:
        result += cur_city * road

        road = 0

result += cur_city * road

print(result)