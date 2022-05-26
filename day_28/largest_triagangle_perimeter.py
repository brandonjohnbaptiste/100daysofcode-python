def largestPerimeter( nums):
    nums.sort(reverse=True)

    for i in range(0, len(nums) - 2):
        if nums[i + 1] + nums[i + 2] > nums[i]:
            return nums[i + 1] + nums[i + 2] + nums[i]
    return 0
