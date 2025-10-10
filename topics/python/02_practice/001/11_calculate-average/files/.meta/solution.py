def calculateAverage(numbers):
    if len(numbers) == 0:
        return 0

    total = sum(numbers)
    return total / len(numbers)
