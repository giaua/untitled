import os
txt = []
with open(os.path.join('C:\py3eg\input.txt'), 'r') as inf:
    for line in inf:
        txt.append([i.strip() for i in line.split(';')])
"""x = int(input())
txt = [[0 for j in range(4)] for i in range(x)]
for i in range(x):
    txt[i] = ([k for k in input().split()])"""
dic = {}
print(txt)
for i in txt:
    if i == '3':
        continue
    if i[0] in dic:
        if i[1] > i[3]:
            dic[i].append()

