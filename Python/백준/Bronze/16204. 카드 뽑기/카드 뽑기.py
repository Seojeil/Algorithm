import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

print(min(M, K) + min(N-M, N-K))