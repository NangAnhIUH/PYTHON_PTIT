BASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    n = input()
    if n == "0":
        break
    k, s = n.split()
    k = int(k)
    cypher = BASE[k:] + BASE[:k]
    print(*list(cypher[BASE.index(c)] for c in s)[::-1], sep="")