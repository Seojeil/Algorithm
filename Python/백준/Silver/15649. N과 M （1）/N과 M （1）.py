import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

result = list(permutations(range(1, N+1), M))

for r in result:
    print(*r)