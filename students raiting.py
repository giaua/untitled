import os
x = []
with open(os.path.join('/Users/admin/Documents/python/dataset_3363_4.txt'), 'r') as inf:
    for line in inf:
        y = [i.strip() for i in line.split(';')]
        x.append(y)
dic = {}
for i in range(len(x)):
    k = x[i][0]
    for j in range(1, len(x[i])):
        if k in dic:
            dic[k].append(float(x[i][j]))
        else:
            dic[k] = [float(x[i][j])]
z = 0
v = 0
c = 0
l = 0
with open(os.path.join('/Users/admin/Documents/python/output.txt'), 'w') as ouf:
    for value in dic.values():
        k = 0
        j = 0
        for i in  value:
            k += i
            j += 1
        #value.append(k / j)    осталось от добавления в словарь
        ouf.write(str(k / j))
        ouf.write('\n')
        z += value[0]
        v += value[1]
        c += value[2]
        l += 1
    dic['Total'] = [z / l, v / l, c / l]
    for i in dic['Total']:
        ouf.write(str(i))
        ouf.write(' ')