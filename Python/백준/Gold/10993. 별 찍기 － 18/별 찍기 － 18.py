import sys

N = int(sys.stdin.readline())


def stars(n):
    if n == 1:
        return '*'

    new_stars = []

    row = (2**n - 1) * 2 - 1
    col = 2**n - 1

    if n % 2 == 0:
        new_stars.append('*' * row)

        for i in range(1, col - 1):
            new_stars.append(' ' * i + '*' + ' ' * (row - 2 - i * 2) + '*')

        new_stars.append(' ' * (col - 1) + '*')

    else:
        new_stars.append(' ' * (col - 1) + '*')

        for i in range(1, col - 1):
            new_stars.append(' ' * (col - 1 - i) + '*' + ' ' * (i * 2 - 1) + '*')

        new_stars.append('*' * row)

    small_star = stars(n-1)

    if n % 2 == 0:
        for i, s in enumerate(small_star):
            original = new_stars[i+1]
            new_stars[i+1] = original[:2**(n-1)] + s + original[2**(n-1)+len(s):]

    else:
        for i, s in enumerate(small_star):
            original = new_stars[col//2 + i]
            new_stars[col//2 + i] = original[:2**(n-1)] + s + original[2**(n-1)+len(s):]

    return new_stars


result = stars(N)

for s in result:
    print(s)