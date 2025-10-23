def formatLikes(names):
    count = len(names)

    if count == 0:
        return "no one likes this"
    elif count == 1:
        return f"{names[0]} likes this"
    elif count == 2:
        return f"{names[0]} and {names[1]} like this"
    elif count == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        others = count - 2
        return f"{names[0]}, {names[1]} and {others} others like this"
