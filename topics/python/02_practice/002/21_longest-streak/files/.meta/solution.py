def longestStreak(numbers):
    if len(numbers) == 0:
        return 0

    max_streak = 1
    current_streak = 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i-1] + 1:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1

    return max_streak
