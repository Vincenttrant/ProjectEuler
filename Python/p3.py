import math

def primeFactor(n):
    max = 2

    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            max = i
            n //= i
    
    return max

if __name__ == "__main__":
    print(primeFactor(600851475143))