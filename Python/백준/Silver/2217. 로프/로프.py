import sys
from collections import deque

N = int(sys.stdin.readline())

ropes = []

for _ in range(N):
    ropes.append(int(sys.stdin.readline()))

ropes = deque(sorted(ropes))

result = []

while ropes:
    rope = ropes.popleft()

    result.append(rope * (len(ropes) + 1))

print(max(result))
