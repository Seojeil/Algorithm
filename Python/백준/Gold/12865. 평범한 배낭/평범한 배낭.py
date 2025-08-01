import sys

input = sys.stdin.readline

N, K = map(int, input().split())

items = []

for _ in range(N):
    items.append(tuple(map(int, input().split())))

def bag(items, n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n+1):
        w, v = items[i-1]
        
        for j in range(1, k+1):
            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
    
    return dp[n][k]

print(bag(items, N, K))