def is_happy(n):
    prev_num = []
    happy = False

    while not happy:
        digits = [int(num) for num in str(n)]
        sum = 0

        for i in digits:
            sum += i * i

        if sum in prev_num:
            return False
        if sum == 1:
            happy = True
            return True

        n = sum
        prev_num.append(sum)

