from collections import deque

S = int(input())
sol = 10001
que = deque([[1, 0, 0]])
vst = [[0] * 1001 for _ in range(1001)]
while que:
    imoji, clip, ln = que.popleft()
    if sol > ln:
        if imoji == S:
            sol = ln
            break
        if clip:
            i, c = imoji + clip, clip
            if 0 < i < 1001 and not vst[i][c]:
                vst[i][c] = 1
                que.append([i, c, ln+1])
        for i, c in [[imoji, imoji], [imoji-1, clip]]:
            if 0 < i < 1001 and not vst[i][c]:
                vst[i][c] = 1
                que.append([i, c, ln+1])
print(sol)