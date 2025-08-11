import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())

result = list(product(range(1, N+1), repeat=M))

for r in result:
    print(*r)