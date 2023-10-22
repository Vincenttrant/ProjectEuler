def smallestMultiple(n):
    i = n
    while True:
        for j in range(1, n+1):
            if i % j != 0:
                break
            if j == n:
                return i
        i += 1
if __name__ == "__main__":
    print(smallestMultiple(20))