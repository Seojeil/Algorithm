import sys
input = sys.stdin.readline

T = int(input())


def fibonacci_dp(n):
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1

    zero = [0]*(n+1)
    one = [0]*(n+1)

    zero[0] = 1
    one[0] = 0

    zero[1] = 0
    one[1] = 1

    for i in range(2, n+1):
        zero[i] = zero[i-1] + zero[i-2]
        one[i] = one[i-1] + one[i-2]

    return zero[n], one[n]


for _ in range(T):
    n = int(input())
    zero, one = fibonacci_dp(n)
    print(zero, one)