import requests
import os
with open(os.path.join('/Users/admin/Documents/python/dataset_3378_3.txt'), 'r') as inf:
    url = inf.readline().strip()
first = requests.get(url).text[:2]
while first != 'We':
    file_name = requests.get(url).text
    first = requests.get(url).text[:2]
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + file_name
    print(file_name)
with open(os.path.join('/Users/admin/Documents/python/output.txt'), 'w') as ouf:
    ouf.write(file_name)
    ouf.write()