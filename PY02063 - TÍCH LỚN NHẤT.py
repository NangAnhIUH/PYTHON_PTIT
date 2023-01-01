n = int(input())
max1, max2, max3 = [-1000] * 3
min1, min2 = [1000] * 2

for i in map(int, input().split()):
    if i >= max1:
        max1, max2, max3 = i, max1, max2
    elif i >= max2:
        max2, max3 = i, max2
    elif i > max3:
        max3 = i

    if i <= min1:
        min1, min2 = i, min1
    elif i < min2:
        min2 = i

print(max(max1 * max2 * max3,
          max1 * min1 * min2))
