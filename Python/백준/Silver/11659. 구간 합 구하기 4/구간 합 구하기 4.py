import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)

for k in range(N):
    prefix_sum[k+1] = prefix_sum[k] + numbers[k]

for _ in range(M):
    i, j = map(int, input().split())
    
    print(prefix_sum[j] - prefix_sum[i-1])