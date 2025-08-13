import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [int(input()) for _ in range(N)]
dice = [int(input()) for _ in range(M)]
location = 0
result = 0

for d in dice:
    location += d
    result += 1
    
    if location >= N:
        break
    
    location += board[location]

    if location >= N:
        break


print(result)