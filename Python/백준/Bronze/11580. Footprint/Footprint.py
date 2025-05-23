import sys

_ = sys.stdin.readline()

move = sys.stdin.readline().strip()

d = {'E': (1, 0), 'W': (-1, 0), 'S': (0, -1), 'N': (0, 1)}
path = set()
location = (0, 0)
path.add(location)

for m in move:
    x, y = location
    dx, dy = d[m]

    x += dx
    y += dy

    location = (x, y)
    path.add(location)

print(len(path))