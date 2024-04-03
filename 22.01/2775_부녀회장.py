case = int(input())

for x in range(case):
    floor = int(input())
    num = int(input())
    temp = []
    for i in range(num + 1):
        temp.append(i)
    for j in range(floor):
        for k in range(1, num + 1):
            temp[k] += temp[k - 1]
    print(temp[num])
