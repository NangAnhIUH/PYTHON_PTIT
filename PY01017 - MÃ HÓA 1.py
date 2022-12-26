for _ in range(int(input())):
    s = input()
    count = 1
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            print(count, s[i - 1], sep="", end="")
            count = 1
        else:
            count += 1
    print(count, s[-1], sep="", end="")
    print()
'''
3
AACDDPQ
11111147g
1111111111
'''