def is_happy(n):
    prev_num = []
    happy = False

    while not happy:
        digits = [int(num) for num in str(n)]
        sum = 0

        for i in digits:
            sum += i * i

        print(sum)
        break

is_happy(12345)