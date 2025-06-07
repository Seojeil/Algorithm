import sys

input = sys.stdin.readline

while True:
    i = list(map(int, input().split()))

    N = i[0]

    if N == 0:
        break

    P = i[1]

    result = []

    if P & 1 == 0:
        result.append(P-1)
        result.append(N - (P-1))
        result.append(N - (P-1) + 1)
    else:
        result.append(P+1)
        result.append(N - P)
        result.append(N - P + 1)

    result.sort()

    print(' '.join(map(str, result)))