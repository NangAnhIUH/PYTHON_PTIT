def ThapHaNoi(n, a, b, c):
    if n == 1:
        print(a, "->", c)
    else:
        ThapHaNoi(n-1, a, c, b)
        print(a, "->", c)
        ThapHaNoi(n-1, b, a, c)

ThapHaNoi(int(input()), "A", "B", "C")