def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []

    result = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        result.append(max(window))

    return result
