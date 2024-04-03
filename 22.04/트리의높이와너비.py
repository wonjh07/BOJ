import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 노드 전체를 탐색해서 최초 root를 찾아줌
def root_finder(x):
    global cot
    if x <= N:
        l, r = V[x]
        if l != -1:
            root_finder(l)
        if r != -1:
            root_finder(r)
        cot += 1

# 중위 순회로 각노드별 인덱스 부여
def in_order(x, lv):
    global cnt
    if x <= N:
        l, r = V[x]
        if l != -1:
            in_order(l, lv+1)
        W[lv].append(cnt)
        cnt += 1
        if r != -1:
            in_order(r, lv+1)


N = int(input())
root = 0
V = [() for _ in range(N+1)]
W = [[] for _ in range(N+1)]

for _ in range(N):
    cnt = 1
    a, b, c = map(int, input().split())
    V[a] = (b, c)

for i in range(1, N+1):
    cot = 0
    root_finder(i)
    if cot == N:
        root = i  # 루트노드 발견
        break

in_order(root, 1)

s_lv = 1  # 루트노드 레벨
mx_w = 1  # 루트노드 너비
for lv in range(2, N+1):
    if W[lv]:
        if len(W[lv]) == 1:
            tmp = 1
        else:
            tmp = max(W[lv]) - min(W[lv]) + 1
        
        if mx_w < tmp:
            mx_w = tmp
            s_lv = lv

print(s_lv, mx_w)
print(W)