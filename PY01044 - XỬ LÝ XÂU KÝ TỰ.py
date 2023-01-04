A = []
s1 = set(c.lower() for c in input().split())
s2 = set(c.lower() for c in input().split())
print(*sorted(s1.union(s2)))
print(*sorted(s1.intersection(s2)))