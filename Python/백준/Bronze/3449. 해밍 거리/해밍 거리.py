T = int(input())

for _ in range(T):
    A = input()
    B = input()

    X = 0

    for a, b in zip(A, B):
        if a != b:
            X += 1
    print(f'Hamming distance is ' + str(X) + '.')