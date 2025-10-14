def abbreviateName(name):
    words = name.split()
    first_initial = words[0][0].upper()
    last_initial = words[1][0].upper()
    return f"{first_initial}.{last_initial}"
