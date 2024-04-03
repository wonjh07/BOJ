import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solution():
    N, M = map(int, input().rstrip().split())
    indegree = [0] * (N + 1)
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        nums = list(map(int, input().rstrip().split()))
        for i in range(1, nums[0]):
            graph[nums[i]].append(nums[i+1])
            indegree[nums[i+1]] += 1

    q = deque([])
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    ans = []
    while q:
        idx = q.popleft()
        ans.append(idx)
        for num in graph[idx]:
            indegree[num] -= 1
            if not indegree[num]:
                q.append(num)
    if max(indegree) != 0:
        print(0)
    else:
        print(*ans, sep='\n')
    return
solution()
