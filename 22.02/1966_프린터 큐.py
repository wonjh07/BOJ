import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().rstrip().split())
    docs = list(map(int, input().rstrip().split()))
    order_docs = sorted(docs, reverse=True)
    count = 1
    a = docs[M]
    docs[M] = 'x'
    while docs:
        if docs[0] == 'x':
            if order_docs[0] == a:
                print(count)
                break
            else:
                docs.append(docs.pop(0))

        elif docs[0] == order_docs[0]:
            docs.pop(0)
            order_docs.pop(0)
            count += 1
        else:
            docs.append(docs.pop(0))
