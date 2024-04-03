import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solution():
    N = int(input())

    def path_sort():
        planets = [list(map(int, input().split())) + [n] for n in range(N)]
        temp = []
        for t in range(3):
            planets.sort(key=lambda x: x[t])
            for p1 in range(N-1):
                dist = min([abs(planets[p1][t] - planets[p1+1][t])])
                temp.append((planets[p1][-1], planets[p1+1][-1], dist))
        return sorted(temp, key=lambda x: x[2])

    parent = [i for i in range(N)]
    ans, cnt = 0, 0
    graph = path_sort()

    def get_parent(idx):
        while parent[idx] != idx:
            idx = parent[idx]
        return idx

    def union_parent(n1, n2):
        a, b = get_parent(n1), get_parent(n2)
        if a == b:
            return 0
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return 1

    for n1, n2, d in graph:
        if union_parent(n1, n2):
            ans += d
            cnt += 1
        if cnt == N - 1:
            break

    print(ans)
    return
solution()
