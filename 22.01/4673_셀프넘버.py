def d(n):
    num = str(n)
    for i in range(len(num)):
        n += int(num[i])
    return n


not_self_nums = []
for j in range(1, 10000):
    not_self_nums.append(d(j))

for k in range(1, 10000):
    if k not in not_self_nums:
        print(k)
