import sys, heapq
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    hq = []
    rv_hq = []
    wait_hq = []
    wait_rv_hq = []
    l = 0
    for _ in range(N):
        order, num = input().rstrip().split(' ')
        num = int(num)
        if order == 'I':
            l += 1
            heapq.heappush(hq, num)
            heapq.heappush(rv_hq, -num)

        elif hq:
            l -= 1
            if (num == -1):
                temp = heapq.heappop(hq)
                heapq.heappush(wait_rv_hq, -temp)

                while wait_hq:
                    if wait_hq[0] == hq[0]:
                        heapq.heappop(wait_hq)
                        heapq.heappop(hq)
                    else:
                        break

            elif(num == 1):
                temp = heapq.heappop(rv_hq)
                heapq.heappush(wait_hq, -temp)

                while wait_rv_hq:
                    if wait_rv_hq[0] == rv_hq[0]:
                        heapq.heappop(wait_rv_hq)
                        heapq.heappop(rv_hq)
                    else:
                        break

        if l == 0:
            hq = []
            rv_hq = []
            wait_hq = []
            wait_rv_hq = []

    if not hq:
        print('EMPTY')
    else:
        print(-rv_hq[0], hq[0])