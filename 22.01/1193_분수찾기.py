case = int(input())
count = 0
result = 0
while result < case:
    result += count
    count += 1

a = count - 1
b = 1
for i in range(result - case):

    a -= 1
    b += 1

if (count - 1) % 2:
    print(f"{b}/{a}")
else:
    print(f"{a}/{b}")
