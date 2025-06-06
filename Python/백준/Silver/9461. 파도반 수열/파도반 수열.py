import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    dp = [1] * (N+1)

    if N <= 3:
        print(1)
    else:
        for i in range(4, N+1):
            dp[i] = dp[i-2] + dp[i-3]
        print(dp[N])