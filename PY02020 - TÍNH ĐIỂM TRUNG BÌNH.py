unuse, a =input(), list(map(float, input().split()))
low, high = min(a), max(a)
a = [x for x in a if low < x < high]
print(f"{sum(a) / len(a):.2f}")