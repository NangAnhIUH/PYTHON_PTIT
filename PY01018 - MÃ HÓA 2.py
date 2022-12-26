P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    n = input()
    if n == "0":
        break
    K, S = n.split()
    K = int(K)
    S = S[::-1]
    new_P = P[K:] + P[:K]
    # print(new_P)
    for i in range(len(S)):
        print(new_P[P.index(S[i])], end="")
    print()