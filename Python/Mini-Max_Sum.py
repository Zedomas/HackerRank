def miniMaxSum(arr):
    x = sorted(arr)
    min = x[0] + x[1] + x[2] + x[3]
    max = x[1] + x[2] + x[3] + x[4]
    print(min, max)
