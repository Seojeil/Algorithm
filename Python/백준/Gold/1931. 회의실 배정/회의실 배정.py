N = int(input())

meetings = []

for _ in range(N):
    meetings.append(tuple(map(int, input().split())))

meetings.sort(key=lambda x: (x[1], x[0]))
end_time = 0
result = 0

for meeting in meetings:
    if meeting[0] >= end_time:
        end_time = meeting[1]
        result += 1

print(result)
