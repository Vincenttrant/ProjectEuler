def sumSquare(n):
    sum = 0
    square = 0

    for i in range(1, n + 1):
        sum += pow(i, 2)
        square += i
    square = pow(square, 2)

    return square - sum

if __name__ == "__main__":
    print(sumSquare(100))