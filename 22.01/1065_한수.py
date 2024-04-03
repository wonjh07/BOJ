def hannum(num):
    temp = []
    for j in str(num):
        temp.append(int(j))
    if num <= 99:
        return 1
    elif temp[1] - temp[0] == temp[2] - temp[1]:
        return 1
    else:
        return 0


case = int(input())
count = 0
for i in range(1, case + 1):
    if hannum(i) == 1:
        count += 1
print(count)
