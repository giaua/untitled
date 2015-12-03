import os
x = x1 = x2 = x3 = 0
ouf = open(os.path.join('/Users/admin/Documents/python/output.txt'), 'w')
with open(os.path.join('/Users/admin/Documents/python/dataset_3363_4.txt'), 'r') as inf:
    for line in inf:
        y = [i.strip() for i in line.split(';')]
        x1 += float(y[1])
        x2 += float(y[2])
        x3 += float(y[3])
        for j in range(1, len(y)):
            x += float(y[j])
        ouf.write(str(x / 3))
        x = 0
        ouf.write('\n')
    ouf.write(str(x1))
    ouf.write(' ')
    ouf.write(str(x2))
    ouf.write(' ')
    ouf.write(str(x3))
    ouf.write('\n')
ouf.close()