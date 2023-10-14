def M35(length):
    sum = 0
    for i in range(1, length):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum
    
if __name__ == "__main__":
    length = 1000
    print(M35(length))
