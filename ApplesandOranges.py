def countApplesAndOranges(s, t, a, b, apples, oranges):
    acount = 0
    ocount = 0
    for x in apples:
        if a+x >= s and a+x <= t:
            acount += 1
    for x in oranges:
        if b+(x) <= t and b+(x) >= s:
            ocount += 1
    print(acount)
    print(ocount)