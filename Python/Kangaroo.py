def kangaroo(x1, v1, x2, v2):
    if v2 >= v1:
        return("NO")
    else:       
        while x1 <= x2:
            print(x1, x2)   
            if x1 == x2:
                return("YES")
            else:
                x1 += v1
                x2 += v2
        return("NO")