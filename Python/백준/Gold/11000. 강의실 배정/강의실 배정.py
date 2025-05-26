import heapq
import sys
input = sys.stdin.readline

N = int(input())

lectures = []

for _ in range(N):
    lectures.append(tuple(map(int, input().split())))

lectures.sort(key=lambda x: (x[0], x[1]))

room = []

for lecture in lectures:
    if room and room[0] <= lecture[0]:
        heapq.heappop(room)
    heapq.heappush(room, lecture[1])

print(len(room))
