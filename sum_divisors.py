def sum_divisors(n):
    sum = 0
    i = 1
    while i < n:
        if (n % i) == 0:
            sum = sum + i
        i+=1
        #return sum
    return sum
print(sum_divisors(0))
print(sum_divisors(3))
print(sum_divisors(36))
print(sum_divisors(102))

