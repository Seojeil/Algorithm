import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

N, M = map(int, input().split())

result = list(combinations_with_replacement(range(1, N+1), M))

for r in result:
    print(*r)