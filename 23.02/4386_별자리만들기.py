import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solution():
    n = int(input())
    graph = []
    cnt, cost = 0, 0
    parent = [p for p in range(n)]
    def get_graph():
        arr = [tuple(map(float, input().rstrip().split())) for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                graph.append((i, j, round(((arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2) ** 0.5, 2)))
        graph.sort(key=lambda x: x[2])
        return
    
    def find_parent(v):
        while parent[v] != v:
            v = parent[v]
        return v

    def union_parent(v1, v2):
        a, b = find_parent(v1), find_parent(v2)
        if a == b:
            return 0
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
        return 1

    get_graph()
    for v1, v2, d in graph:
        if union_parent(v1, v2):
            cnt += 1
            cost += d
        if cnt == n-1:
            break

    print(cost)
    return
solution()