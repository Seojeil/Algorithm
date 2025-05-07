import sys
sys.setrecursionlimit(1000000)

def fib(k, memo={}):
    if k in memo:
        return memo[k]
    if k == 1 or k == 2:
        return 1
    else:
        result = fib(k-1) + fib(k-2)
        memo[k] = result
        return result

def solution(n):
        
    return (fib(n)) % 1234567