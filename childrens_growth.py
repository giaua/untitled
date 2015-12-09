import os
dic = {}
print(dic)
ins = []
with open(os.path.join('/Users/admin/Documents/python/dataset_3380_5.txt'), 'r') as inf:
    for line in inf:
        print(line)
        ins = [i for i in line.split()]
        ins[0] = int(ins[0])
        if ins[0] in dic.keys():
            dic[ins[0]][0] += 1
            dic[ins[0]][1] += int(ins[2])
        else:
            dic[ins[0]] = [1, int(ins[2])]
print(dic)
with open(os.path.join('/Users/admin/Documents/python/output.txt'), 'w') as ouf:
    for i in range(1, 12):
        if i in dic.keys():
            ouf.write((str(i) + ' ' + str(dic.get(i)[1] / dic.get(i)[0])))
        else:
            ouf.write((str(i) + ' ' + '-'))
        ouf.write('\n')