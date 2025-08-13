import sys

input = sys.stdin.readline

N = int(input())

K = 1
result = 0

while N:
    N -= K
    result += 1
    
    if K+1 > N:
        K = 1
    else:
        K += 1

print(result)