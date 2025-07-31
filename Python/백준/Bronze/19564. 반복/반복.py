text = input()

result = 1

current_text = ord(text[0])

for t in text[1:]:
    if ord(t) <= current_text:
        result += 1

    current_text = ord(t)

print(result)