import sys
input = sys.stdin.readline

N, M = map(int, input().split())
temperature = list(map(int, input().split()))

prefix_sum = [0] * (N-M+1)

prefix_sum[0] = sum(temperature[:M])

for i in range(N-M):
    prefix_sum[i+1] = prefix_sum[i] + temperature[M+i] - temperature[i]

print(max(prefix_sum))