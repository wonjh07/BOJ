import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


def main():
    V, E = map(int, input().rstrip().split())
    parrent = [i for i in range(V+1)]
    cnt, cost = 0, 0
    arr = sorted([tuple(map(int, input().rstrip().split()))
                 for _ in range(E)], key=lambda x: x[2])

    def get_parrent(idx):
        if parrent[idx] != idx:
            result = get_parrent(parrent[idx])
            parrent[idx] = result
            return result
        else:
            return idx

    def union(v1, v2):
        a, b = get_parrent(v1), get_parrent(v2)
        if a == b:
            return False
        if a > b:
            parrent[a] = b
        else:
            parrent[b] = a
        return True

    for v1, v2, n in arr:
        if union(v1, v2):
            cnt += 1
            cost += n
        if cnt == V-1:
            break

    print(cost)
    return


main()
