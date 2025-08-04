import sys

input = sys.stdin.readline

N = int(input())

triangle = [list(map(int, input().split())) for _ in range(N)]

dp = [[] for _ in range(N)]

dp[0] = triangle[0]

for i in range(1, N):
    dp[i].append(dp[i-1][0] + triangle[i][0])
    for j in range(1, len(triangle[i])-1):
        dp[i].append(max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])
    dp[i].append(dp[i-1][i-1] + triangle[i][i])

print(max(dp[N-1]))