n = int(input())
start = 666
count = 1
while 1:
	if count == n + 1:
		print(start - 1)
		break
	if '666' in str(start):
		count += 1
	start += 1