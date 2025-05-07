word = input().upper()

result = {}

for w in set(word):
    c = word.count(w)

    if c in result:
        result[c].append(w)
    else:
        result[c] = [w]

m = max(result.keys())

if len(result[m]) == 1:
    print(result[m][0])
else:
    print('?')