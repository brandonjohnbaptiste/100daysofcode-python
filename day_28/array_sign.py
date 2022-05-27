from math import prod


def arraySign(nums):
    sign = 1 if prod(nums) > 0 else -1
    return 0 if prod(nums) == 0 else sign
