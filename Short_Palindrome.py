def shortPalindrome(s):
    mod = 10000000007
    count = 0
    for x in range(len(s)):
        for y in range(x+1, len(s)):
            for z in range(y+1, len(s)):
                if s[y] == s[z]:
                    count += s[z+1:].count(s[x])
                    print(count)
                    return (count * 2) % mod