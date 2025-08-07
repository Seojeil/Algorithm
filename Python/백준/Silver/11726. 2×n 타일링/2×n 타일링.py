import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)

def tile(n):
    if n == 1 or n == 2:
        return n

    dp[1] = 1
    dp[2] = 2

    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(tile(N) % 10_007)