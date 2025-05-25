import sys

N = int(sys.stdin.readline())

ropes = []

for _ in range(N):
    ropes.append(int(sys.stdin.readline()))

ropes.sort()

result = 0

for i in range(N):
    cur_weight = ropes[i] * (N-i)

    result = max(result, cur_weight)

print(result)
