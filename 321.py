import os
y = []
x = []
s = set()
with open(os.path.join('/Users/admin/Documents/python/dataset_3363_3.txt'), 'r') as inf:
    for line in inf:
        y = [i.lower() for i in line.split()]
        x.append(y)
y = []
for i in range(len(x)):
    for j in range(len(x[i])):
        s.add(x[i][j])
        y.append(x[i][j])
i = 0
for k in s:
    if y.count(k) > i:
        i = y.count(k)
        j = k
    elif y.count(k) == i:
        if k > j:
            j = k
with open(os.path.join('/Users/admin/Documents/python/output.txt'), 'w') as ouf:
    ouf.write(j)
    ouf.write('')
    ouf.write(str(i))