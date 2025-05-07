import sys
import bisect

input = sys.stdin.readline

N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(int(input()))

A.sort()

for _ in range(M):
    D = int(input())

    pos = bisect.bisect_left(A, D)

    if pos < len(A) and A[pos] == D:
        print(pos)
    else:
        print(-1)