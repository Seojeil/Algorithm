C = int(input())

result = 0

for _ in range(C):
    code = input()
    result = max(result, code.count('for') + code.count('while'))

print(result)