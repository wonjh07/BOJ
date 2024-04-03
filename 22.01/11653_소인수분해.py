num = int(input())
temp = []
i = 2
while True:
    if num < i:
        if num != 1:
            temp.append(int(num))
        break
    else:
        if num % i:
            i += 1
        elif not num % i:
            num /= i
            temp.append(i)
for i in sorted(temp):
    print(i)
