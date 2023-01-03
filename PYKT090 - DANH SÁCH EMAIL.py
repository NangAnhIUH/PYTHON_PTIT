D = {}
with open("CONTACT.in", "r") as contact:
    for email in contact.read().split():
        n = email.lower()
        D[n] = D.get(n, n)
L = sorted(D)
print(*L, sep="\n")