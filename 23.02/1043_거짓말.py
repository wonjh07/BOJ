import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def fire_crew(crew, c_vst, lie, party, truth):
    while c_vst[crew]:
        pi = c_vst[crew].pop(-1)
        if lie[pi]:
            lie[pi] = 0
            truth |= party[pi]
            for crew2 in party[pi]:
                if c_vst[crew2]:
                    fire_crew(crew2, c_vst, lie, party, truth)
    return

def main():
    N, M =  map(int, input().rstrip().split())
    truth = set()
    c_vst = [[] for _ in range(N+1)]
    lie = [0] * M

    temp = list(map(int, input().rstrip().split()))
    if temp[0]:
        truth.update(temp[1:])

    party = [set(list(map(int, input().rstrip().split()))[1:]) for _ in range(M)]
    for mi in range(M):
        if truth & party[mi]:
            truth |= party[mi]
            for crew in party[mi]:
                if c_vst[crew]:
                    fire_crew(crew, c_vst, lie, party, truth)
        else:
            lie[mi] = 1
            for crew in party[mi]:
                c_vst[crew].append(mi)

    print(sum(lie))
    return

main()

'''
# union-find 풀이법
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def union(x, y, parent):
    a = find_root(parent, x)
    b = find_root(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return

def find_root(parent, idx):
    if parent[idx] == idx:
        return idx
    res = find_root(parent, parent[idx])
    return res

def main():
    N, M =  map(int, input().rstrip().split())
    parent = [i for i in range(N+1)]
    ans = M

    temp = list(map(int, input().rstrip().split()))
    if temp[0]:
        for c in temp[1:]:
            parent[c] = 0

    parties = [list(map(int, input().rstrip().split())) for _ in range(M)]
    for party in parties:
        if party[0] > 1:
            for i in range(1, party[0]):
                union(party[i], party[i+1], parent)

    for party in parties:
        for p in range(1, party[0]+1):
            if parent[find_root(parent, party[p])] == 0:
                ans -= 1
                break

    print(ans)
    return

main()


'''