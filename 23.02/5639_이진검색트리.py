import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readlines

def post(s, e, tree):
    root = tree[s]
    ln = e - s
    if ln == 0:
        print(root)
        return
    left_end = e
    for i in range(s+1, e+1):
        if root < tree[i]:
            left_end = i-1
            break
    if s+1 <= left_end:
        post(s+1, left_end, tree)
    if left_end+1 <= e:
        post(left_end+1, e, tree)
    print(root)
    return

def main():
    tree = list(map(int, ''.join(input()).rstrip().split('\n')))
    print(tree)
    post(0, len(tree)-1, tree)
    return

main()

'''
이진트리를 만들고 다시 읽는 버전
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readlines

def post(tree, k):
    if tree[k][1]:
        post(tree, tree[k][1])
    if tree[k][2]:
        post(tree, tree[k][2])
    print(tree[k][0])

def main():
    arr = list(map(int, ''.join(input()).rstrip().split('\n')))
    tree = [[0, 0, 0] for _ in range(len(arr))]
    tree[0][0] = arr[0]
    j = 0
    for i in range(1, len(arr)):
        while 1:
            if arr[i] < tree[j][0]:
                if not tree[j][1]:
                    tree[j][1] = i
                    tree[i] = [arr[i], 0, 0]
                    break
                else:
                    j = tree[j][1]
            else:
                if not tree[j][2]:
                    tree[j][2] = i
                    tree[i] = [arr[i], 0, 0]
                    break
                else:
                    j = tree[j][2]
    
    post(tree, 0)
    return

main()



'''