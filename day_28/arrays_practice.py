def contains_duplicate(nums):
    return len(nums) != len(set(nums))


def length_of_last_word(s):
    return len(s.split()[-1])
