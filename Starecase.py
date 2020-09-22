def staircase(n):
    for x in range(1, n+1):
        if x < n:
            print((" " * (n - x)) + "#" * x)
        else:
            print("#" * x)