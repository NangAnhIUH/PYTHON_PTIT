import re

A = []
patern = "[0-9]+"

for _ in range(int(input())):
    A.extend(list(map(int, re.findall(patern, input()))))
print(*sorted(A), sep="\n")

