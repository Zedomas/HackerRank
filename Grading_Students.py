def gradingStudents(grades):
    curve = []
    for x in grades:
        if (x+1) % 5 == 0 and x > 38:
            curve.append(x+1)
        elif (x+2) % 5 == 0 and x > 37:
            curve.append(x+2)
        else:
            curve.append(x)
    return curve
