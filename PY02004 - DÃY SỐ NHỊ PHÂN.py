n = int(input())
a = list(map(int, input().split()))
print(len(list(1 for i in range(1, len(a)) if a[i-1] - a[i])))