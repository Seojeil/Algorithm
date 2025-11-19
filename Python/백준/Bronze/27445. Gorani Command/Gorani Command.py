N, M = map(int, input().split())

a = []

for _ in range(N-1):
    a.append(int(input()))

b = list(map(int, input().split()))
a.append(b[0])

r = 1
c = 1

for i in range(N-1):
    if a[i] > a[i+1]:
        r += 1
    else:
        break

for i in range(M-1):
    if b[i] > b[i+1]:
        c += 1
    else:
        break

print(r, c)