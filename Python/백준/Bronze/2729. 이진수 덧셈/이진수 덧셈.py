import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    i, j = map(int, input().split())

    result = int(str(i), 2) + int(str(j), 2)

    print(bin(result)[2:])