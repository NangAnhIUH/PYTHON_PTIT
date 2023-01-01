a = []

for i in range(int(input())):
    s = input()
    c, t = map(int, input().split())
    a.append((c, t, s))
a.sort(key=lambda x: (-x[0], x[1], x[2]))

for x in a:
    print(f'{x[2]} {x[0]} {x[1]}')
