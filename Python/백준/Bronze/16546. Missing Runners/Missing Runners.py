import sys

input = sys.stdin.readline

N = int(input())

start = set(range(1, N + 1))

arrival = set(map(int, input().split()))

print((start - arrival).pop())