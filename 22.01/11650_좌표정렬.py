import sys

case = int(sys.stdin.readline())
list_1 = [''] * 200001

for i in range(case):
	a, b = list(map(int, sys.stdin.readline().split()))
	list_1[a] += str(b) + ' '

for j in range(-100000,100001):
	for k in sorted(list(map(int, list_1[j].split()))):
		if k is not None:
			print(j, k)
