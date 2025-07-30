import sys

input = sys.stdin.readline

X = int(input())

def calculation(number):
    dp = [float('inf')] * (number + 1)
    dp[0] = 0
    dp[1] = 0

    for i in range(2, number + 1):
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)
    
        dp[i] = min(dp[i], dp[i-1]+1)
    
    return dp[number]

print(calculation(X))