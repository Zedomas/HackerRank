def timeConversion(s):
    x = s.split(":")
    h = int(x[0])
    if "PM" in x[2]:
        if h < 12:
            h += 12
        x[2] = x[2][:-2]
        return (str(h) + ":" + x[1] + ":" + x[2])
    x[2] = x[2][:-2]
    if h == 12:
        x[0] = "00"
    return (x[0] + ":" + x[1] + ":" + x[2])
    