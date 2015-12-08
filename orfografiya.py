x = int(input())
correct = []
check = []
result = set()
for i in range(x):
    correct.append(input())
y = int(input())
for i in range(y):
    check.append([i for i in input().split()])
for i in range(len(check)):
    for j in range(len(check[i])):
        if correct.count(check[i][j]) == 0:
            result.add(check[i][j])
for i in result:
    print(i)