x = int(input())
spis_in = []
dic_res = {}
for i in range(x):
    spis_in.append([str(i) for i in input().split()])
for i in spis_in:
    if i[0] not in dic_res:
        dic_res[i[0]] = int(i[1])
    else:
        dic_res[i[0]] += int(i[1])
y = dic_res['восток'] - dic_res['запад']
z = dic_res['север'] - dic_res['юг']
print(y, z, sep=' ')
