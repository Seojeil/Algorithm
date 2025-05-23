import sys

N = int(sys.stdin.readline())

for _ in range(N):
    result = 0

    M = int(sys.stdin.readline())

    mission = []

    for _ in range(M):
        mission.append(map(int, sys.stdin.readline().split()))

    k, d, a = map(int, sys.stdin.readline().split())

    for m in mission:
        K, D, A = m

        score = K*k - D*d + A*a

        if score > 0:
            result += score

    print(result)
