def moveZeros(numbers):
    non_zeros = []
    zero_count = 0

    for num in numbers:
        if num == 0:
            zero_count += 1
        else:
            non_zeros.append(num)

    return non_zeros + [0] * zero_count
