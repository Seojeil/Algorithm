import sys

input = sys.stdin.readline

N, K = map(int, input().split())

unsold = [0]

for _ in range(N):
    A, B = map(int, input().split())

    if A - B >= 0:
        K -= 1
    else:
        unsold.append(B-A)

unsold.sort()

if K <= 0:
    K = 0

print(unsold[K])