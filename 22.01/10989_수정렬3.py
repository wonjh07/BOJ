import sys

n = int(sys.stdin.readline())
max = 0
n_dict = [0]*10001
for i in range(n):
	x = int(sys.stdin.readline())
	if x > max:
		max = x
	n_dict[x] += 1

i = 1
while i <= max:
	if n_dict[i] > 0:
		print(i)
		n_dict[i] -= 1
	else:
		i+=1
