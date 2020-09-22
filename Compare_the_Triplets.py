def compareTriplets(a, b):
    acount = 0
    bcount = 0
    for x in range(3):
        if a[x] > b[x]:
            acount += 1
        elif b[x] > a[x]:
            bcount += 1
    return acount, bcount
