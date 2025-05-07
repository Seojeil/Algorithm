N = int(input())

a = 1
b = 1

if N <= 4:
    result = 1
else:
    while (a+1) * (b+1) < N:
        a += 1
        if (a+1) * (b+1) >= N:
            break
        b += 1
print((a+b) * 2)