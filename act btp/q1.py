def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num): 
        if num % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    return [x for x in range(2, n + 1) if is_prime(x)]

n = int(input("Enter a number: "))
print(getPrimeNumbers(n))
