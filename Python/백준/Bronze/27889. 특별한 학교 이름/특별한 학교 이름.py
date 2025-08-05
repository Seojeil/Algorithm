import sys

input = sys.stdin.readline

title = input().strip()

abbreviation = {"NLCS":"North London Collegiate School", "BHA":"Branksome Hall Asia", "KIS":"Korea International School", "SJA":"St. Johnsbury Academy"}

print(abbreviation[title])