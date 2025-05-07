def is_prime(n):
    if n <= 1:
        return False

    if n % 2 == 0:
        return False

    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def solution(nums):
    answer = 0
    sums = []
    l = len(nums)
    
    for n in range(l):
        for k in range(n+1, l):
            for i in range(k+1, l):
                sums.append(nums[n]+nums[k]+nums[i])
    
    for n in sums:
        if is_prime(n):
            answer += 1
    
    return answer