T = int(input())

for _ in range(T):
    N, D = map(int, input().split())

    n = 0

    for _ in range(N):
        v, f, c = map(int, input().split())

        if v * f / c >= D:
            n += 1

    print(n)