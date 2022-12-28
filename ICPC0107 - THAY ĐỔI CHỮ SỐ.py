for _ in range(int(input())):
    P, Q = input().split()
    x1 = input().split()
    if len(x1) > 1:
        x1, x2 = x1[0], x1[1]
    else:
        x1 = x1[0]
        x2 = input()
    a = sum(map(int,[x1.replace(P, Q), x2.replace(P, Q)]))
    b = sum(map(int,[x1.replace(Q, P), x2.replace(Q, P)]))
    print(min(a, b), max(a, b))