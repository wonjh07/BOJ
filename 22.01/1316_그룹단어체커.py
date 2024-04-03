case = int(input())
count = case
for i in range(case):
    word = input()
    temp = []
    current = ''
    for j in word:
        if j != current and j not in temp:
            temp.append(j)
            current = j
        elif j != current and j in temp:
            count -= 1
            break
print(count)
