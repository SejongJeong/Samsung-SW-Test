from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
mov_x = (1, 0, -1, 0)
mov_y = (0, -1, 0, 1)
q = deque()
rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
	for j in range(M):
		if board[i][j] == 'R':
			rx, ry = j, i
		elif board[i][j] == 'B':
			bx, by = j, i
q.append((rx, ry, bx, by, 1))
visited[ry][rx][by][bx] = True


def mov(rx, ry, bx, by, d):
	r_cnt, b_cnt = 0, 0
	while board[ry + mov_y[d]][rx + mov_x[d]] != '#' and board[ry][rx] != 'O':
		rx += mov_x[d]
		ry += mov_y[d]
		r_cnt += 1
	while board[by + mov_y[d]][bx + mov_x[d]] != '#' and board[by][bx] != 'O':
		bx += mov_x[d]
		by += mov_y[d]
		b_cnt += 1
	return rx, ry, bx, by, 1 if r_cnt >= b_cnt else 0


def solve():
	while q:
		rx, ry, bx, by, num = q.popleft()
		if num > 10:
			break
		for i in range(4):
			arx, ary, abx, aby, chk = mov(rx, ry, bx, by, i)
			if board[aby][abx] != 'O':
				if board[ary][arx] == 'O':
					print(num)
					return
				if arx == abx and ary == aby:
					if chk == 1:
						arx -= mov_x[i]
						ary -= mov_y[i]
					else:
						abx -= mov_x[i]
						aby -= mov_y[i]
				if visited[ary][arx][aby][abx] is False:
					visited[ary][arx][aby][abx] = True
					q.append((arx, ary, abx, aby, num + 1))
	print(-1)
	return


solve()