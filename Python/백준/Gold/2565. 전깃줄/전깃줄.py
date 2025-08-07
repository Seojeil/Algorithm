import sys

input = sys.stdin.readline

N = int(input())

wires = [tuple(map(int, input().split())) for _ in range(N)]

wires.sort(key=lambda x: x[0])

A = [i[0] for i in wires]
B = [i[1] for i in wires]

dp = [1] * N

for i in range(N):
    for j in range(i):
        if B[i] > B[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))