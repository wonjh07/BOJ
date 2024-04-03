import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def main():
    N, M = map(int, input().rstrip().split())
    parent = [i for i in range(N)]
    ans = 0

    def get_parent(idx):
        while parent[idx] != idx:
            idx = parent[idx]
        return idx

    def union_parent(v1, v2):
        a, b = get_parent(v1), get_parent(v2)
        if a == b:
            return 0
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return 1

    for cnt in range(1, M+1):
        v1, v2 = map(int, input().rstrip().split())
        if not union_parent(v1, v2):
            ans = cnt
            break
    print(ans)

main()