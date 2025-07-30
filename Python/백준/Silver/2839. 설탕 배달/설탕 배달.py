import sys

input = sys.stdin.readline

weight = int(input())

def sugar(weight):
    dp = [float('inf')] * (weight + 1)

    dp[0] = 0

    for i in range(weight + 1):
        if i >= 3:
            if dp[i-3] != -1:
                dp[i] = min(dp[i], dp[i-3]+1)

        if i >= 5:
            if dp[i-5] != -1:
                dp[i] = min(dp[i], dp[i-5]+1)

    if dp[weight] == float('inf'):
        return -1
    else:
        return dp[weight]

print(sugar(weight))