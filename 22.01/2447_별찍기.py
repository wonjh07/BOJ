def print_square(d):
	for j in range(3):
		if j == 1:
			result[j + 3 * d] += '* *'
		else:
			result[j + 3 * d] += '***'


def f_0s(num, d):
	if num == 3:
		for i in range(3):
			result[i + 3 * d] += '   '

	else:
		for k in range(9):
				f_0s(num // 3, k // 3 + 3 * d)


def f_stars(num, d):
	if num == 3:
		print_square(d)

	else:
		for x in range(9):
			if x == 4:
				f_0s(num // 3, x // 3 + 3 * d)
			else:
				f_stars(num // 3, x // 3 + 3 * d)


case = int(input())
result = ['' for x in range(case)]
f_stars(case, 0)
for y in result:
	print(y)