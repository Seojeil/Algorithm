import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    result = 0

    for _ in range(N):
        profit = max(map(int, input().split()))
        
        if profit > 0:
            result += profit

    print(result)