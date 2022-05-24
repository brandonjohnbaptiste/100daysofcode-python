def countOdds(low, high):
    n = (high - low) // 2

    if low % 2 != 0 or high % 2 != 0:
        n += 1

    return n
