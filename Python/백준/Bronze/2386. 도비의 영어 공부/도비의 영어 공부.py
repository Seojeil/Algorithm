import sys

input = sys.stdin.readline

while True:
    text = input().split()

    if text == ['#']:
        break

    cahr = text[0]

    text = list(''.join(text[1:]).lower())

    print(cahr, text.count(cahr))