dic = {}
x = int(input())
for i in range(x):
    team_1, score_1, team_2, score_2 = (i for i in input().split(';'))
    if team_1 not in dic.keys():
        dic[team_1] = [0 for i in range(5)]
    if team_2 not in dic.keys():
        dic[team_2] = [0 for i in range(5)]
    if score_1 > score_2:
        dic[team_1][1] += 1
        dic[team_1][4] += 3
        dic[team_2][3] += 1
    elif score_1 < score_2:
        dic[team_2][1] += 1
        dic[team_2][4] += 3
        dic[team_1][3] += 1
    else:
        dic[team_1][4] += 1
        dic[team_2][4] += 1
        dic[team_1][2] += 1
        dic[team_2][2] += 1
    dic[team_1][0] += 1
    dic[team_2][0] += 1
for key in dic.keys():
    print(key, ':', sep='', end='')
    for i in dic[key]:
        print(i, end=' ')
    print()