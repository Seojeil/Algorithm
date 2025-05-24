S = input()
T = input()


def A_and_B(current, target):
    if current == target:
        return True

    if len(current) <= len(target):
        return False

    if current.endswith('A'):
        if A_and_B(current[:-1], target):
            return True

    if current.startswith('B'):
        if A_and_B(current[1:][::-1], target):
            return True

    return False


if A_and_B(T, S):
    print(1)
else:
    print(0)