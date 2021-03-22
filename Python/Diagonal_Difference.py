def diagonalDifference(arr):
    sumx = 0;
    sumy = 0;
    for i in range(len(arr)):
        sumx += arr[i][i]
        up = ((len(arr) - 1) - i)
        sumy += arr[up][i]
    sum = sumx - sumy
    return abs(sum)