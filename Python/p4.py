def largestPalindrome():
    maxPalindrome = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i * j
            numList = list(str(num))
            reverseList = numList[::-1]
            if numList == reverseList:
                maxPalindrome = max(maxPalindrome, num)
    return maxPalindrome
            
if __name__ == "__main__":
    print(largestPalindrome())