def subarraySum(nums, k):
    count = 0
    current_sum = 0
    sum_count = {0: 1}

    for num in nums:
        current_sum += num
        if current_sum - k in sum_count:
            count += sum_count[current_sum - k]
        sum_count[current_sum] = sum_count.get(current_sum, 0) + 1

    return count
