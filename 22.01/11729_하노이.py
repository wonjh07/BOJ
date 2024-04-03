def hanoi(num):
	if num == 1:
		return 1
	elif num == 2:
		return 3
	return hanoi(num - 1) * 2 + 1


def hanoi_move(num, start, temp, end):
	if num < 1:
		return
	else:
		hanoi_move(num - 1, start, end, temp)
		print(start, end)
		hanoi_move(num - 1, temp, start, end)		

		
case = int(input())
print(hanoi(case))
hanoi_move(case, 1, 2, 3)
