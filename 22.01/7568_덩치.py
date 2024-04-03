people = int(input())
p_list = []
for i in range(people):
	p_list.append(list(map(int, input().split())))
result = []
for a in p_list:
	number = 1
	for b in p_list:
		if (a[0] < b[0]) and (a[1] < b[1]):
			number += 1
	result.append(str(number))
print(' '.join(result))
