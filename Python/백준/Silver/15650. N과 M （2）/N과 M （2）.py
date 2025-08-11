import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

result = list(combinations(range(1, N+1), M))

for r in result:
    print(*r)