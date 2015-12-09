z = int(input())
spis_in = []
x = 0
y = 0
for i in range(z):
    spis_in.append([str(i) for i in input().split()])
for i in spis_in:
    if i[0] == 'восток':
        x += int(i[1])
    elif i[0] == 'запад':
        x -= int(i[1])
    elif i[0] == 'север':
        y += int(i[1])
    elif i[0] == 'юг':
        y -= int(i[1])
print(x, y, sep=' ')