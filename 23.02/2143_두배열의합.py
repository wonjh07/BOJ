import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solution():
    T = int(input())
    ans = 0
    mem = {}

    def find():
        n = int(input())
        lst1 = list(map(int, input().rstrip().split()))
        for i in range(n):
            net = 0
            for j in range(i, n):
                net += lst1[j]
                if not net in mem:
                    mem[net] = 0
                mem[net] += 1
        return
    find()

    m = int(input())
    lst2 = list(map(int, input().rstrip().split()))
    for i in range(m):
        net = 0
        for j in range(i, m):
            net += lst2[j]
            temp = T - net
            if temp in mem:
                ans += mem[temp]
    
    print(ans)
    return
solution()
