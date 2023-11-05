def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def sumPrimeBelow(num):
    sum = 0
    for i in range(2, num):
        if isPrime(i):
            sum += i

    return sum

if __name__ == "__main__":
    print(sumPrimeBelow(2_000_000))