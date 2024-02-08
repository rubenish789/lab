import math

def filterPrime(list):
    primes = []
    for x in list:
        if x < 2:
            continue
        is_prime = True
        i = 2
        while i <= x/2:
            if x % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            primes.append(x)
    return primes

A = list(map(int, input().split()))

print (filterPrime(A))