import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

dp_left = [1] * N
dp_right = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp_left[i] = max(dp_left[i], dp_left[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            dp_right[i] = max(dp_right[i], dp_right[j] + 1)

dp = [(l + r - 1) for l, r in zip(dp_left, dp_right)]

print(max(dp))