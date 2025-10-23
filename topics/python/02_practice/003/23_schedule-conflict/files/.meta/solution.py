def hasConflict(meetings):
    for i in range(len(meetings)):
        for j in range(i + 1, len(meetings)):
            meeting1 = meetings[i]
            meeting2 = meetings[j]

            if meeting1["start"] < meeting2["end"] and meeting2["start"] < meeting1["end"]:
                return True

    return False
