import sys

N = int(sys.stdin.readline())


def stars(n):
    if n == 3:
        return [
            '***',
            '* *',
            '***'
            ]

    prev_pattern = stars(n//3)
    prev_size = n // 3

    new_stars = []

    for star in prev_pattern:
        new_stars.append(star * 3)

    for star in prev_pattern:
        new_stars.append(star + ' ' * prev_size + star)

    for star in prev_pattern:
        new_stars.append(star * 3)

    return new_stars


result = stars(N)

for i in result:
    print(i)