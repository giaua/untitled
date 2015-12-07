import os
with open(os.path.join('/Users/admin/Documents/python/input.txt'), 'r') as inf:
    for line in inf:
        txt = [i.strip(';').split() for i in line]
print(txt)