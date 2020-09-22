def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    l = len(arr)
    for x in arr:
        if x > 0:
            pos += 1
        elif x == 0:
            zero += 1
        elif x < 0:
            neg += 1
    print(pos/l)
    print(neg/l)
    print(zero/l)