orig = input()
key = input()
in_orig = input()
in_crypt = input()
for i in in_orig:
    j = orig.find(i)
    print(key[j], sep='', end='')
print()
for i in in_crypt:
    j = key.find(i)
    print(orig[j], sep='', end='')