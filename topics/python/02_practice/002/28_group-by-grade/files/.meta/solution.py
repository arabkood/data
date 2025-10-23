def groupByGrade(students):
    groups = {}

    for student in students:
        grade = student["grade"]
        name = student["name"]

        if grade in groups:
            groups[grade].append(name)
        else:
            groups[grade] = [name]

    return groups
