import sys

input = sys.stdin.readline

S = int(input())

stairs = []

for _ in range(S):
    stairs.append(int(input()))


def score(stairs, s):
    if s == 1:
        return stairs[0]
    if s == 2:
        return stairs[0] + stairs[1]

    dp = [[0, 0] for _ in range(s)]

    dp[0][0] = stairs[0]
    dp[1][1] = stairs[1]
    dp[1][0] = stairs[0] + stairs[1]

    for i in range(2, s):
        dp[i][0] = dp[i-1][1] + stairs[i]

        dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + stairs[i]

    return max(dp[s-1])


print(score(stairs, S))
