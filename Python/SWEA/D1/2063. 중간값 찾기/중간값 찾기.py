T = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

print(numbers[int((len(numbers) - 1) / 2)])