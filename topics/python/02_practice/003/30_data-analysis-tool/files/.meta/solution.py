def analyzeData(numbers):
    if not numbers:
        return {
            "mean": None,
            "median": None,
            "mode": None,
            "min": None,
            "max": None,
            "range": None
        }

    mean = round(sum(numbers) / len(numbers), 2)

    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    else:
        median = sorted_nums[n // 2]

    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    mode = min([k for k, v in frequency.items() if v == max_freq])

    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "min": min_val,
        "max": max_val,
        "range": range_val
    }
