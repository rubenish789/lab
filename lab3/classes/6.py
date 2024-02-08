def isPrime(number):
    i = 2
    if number < 2:
        return False
    else:
        while i <= number/2:
            if number % i == 0:
                return False
            i += 1
        return True
    

numbers = list(map(int, input("Enter a list: ").split()))

primeNumbers = list(filter(lambda x: isPrime(x), numbers))

print("Prime numbers in your list:", primeNumbers)