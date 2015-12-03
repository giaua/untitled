import os
import requests
with open(os.path.join('/Users/admin/Documents/python/dataset_3378_2.txt'), 'r') as inf:
    url = inf.readline().strip()
print(url)
r = len(requests.get(url).text.splitlines())
print(r)