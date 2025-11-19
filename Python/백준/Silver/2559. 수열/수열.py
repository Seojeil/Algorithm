import sys
input = sys.stdin.readline

N, M = map(int, input().split())
temperature = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)

for k in range(N):
    prefix_sum[k+1] = prefix_sum[k] + temperature[k]

result = []

for i in range(N-M+1):
    result.append(prefix_sum[i+M] - prefix_sum[i])

print(max(result))