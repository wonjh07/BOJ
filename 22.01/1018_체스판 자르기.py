M, N = map(int, input().split())
chess_board = []

for i in range(M):
	chess_board.append([i for i in input()])

result = []
for i in range(M - 7):
	for j in range(N - 7):
		p1 = 0
		p2 = 0
		for k in range(i, i + 8):
			for x in range(j, j + 8):
				if (k + x) % 2 == 0:
					if chess_board[k][x] != 'W':
						p1 += 1
					if chess_board[k][x] != 'B':
						p2 += 1
				else:
					if chess_board[k][x] != 'B':
						p1 += 1
					if chess_board[k][x] != 'W':
						p2 += 1
		result.append(p1)
		result.append(p2)

print(min(result))
