while True:
    try:
        word = input()
    except EOFError:
        break 

    lower, upper, number, blank = 0, 0, 0, 0

    for w in word:
        if w.islower():
            lower += 1
        elif w.isupper():
            upper += 1
        elif w.isdigit():
            number += 1
        elif w == ' ':
            blank += 1

    print(lower, upper, number, blank)