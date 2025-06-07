n = int(input())

for i in range(n):
    word = input().strip()

    shift_word = []

    for char in word:
        shift_word.append(chr(((ord(char) - ord('A')+1) % 26)+ord('A')))

    print(f'String #{i+1}')
    print(''.join(shift_word))
    print('')