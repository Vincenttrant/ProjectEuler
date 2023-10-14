def fibonacci():
    i = [1, 2]
    sum = 0
    while i[0] < 4_000_000:
        if i[0] % 2 == 0:
            sum += i[0]
        i[0], i[1] = i[1], i[0] + i[1]
        # temp = i[0] + i[1]
        # i[0] = i[1]
        # i[1] = temp
        
    return sum

if __name__ == "__main__":
    print(fibonacci())