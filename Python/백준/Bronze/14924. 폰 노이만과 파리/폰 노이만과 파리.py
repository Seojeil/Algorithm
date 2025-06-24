import sys

input = sys.stdin.readline

S, T, D = map(int, input().split())

print((D//(S*2)) * T)