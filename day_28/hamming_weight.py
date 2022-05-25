def hammingWeight(n):
    num = 0
    while n:
        n &= (n - 1)
        num += 1

    return num
