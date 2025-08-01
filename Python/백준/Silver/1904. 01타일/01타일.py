import sys

input = sys.stdin.readline

N = int(input())

def tile(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0] * (n+1)
    
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746

    return dp[n]

print(tile(N))