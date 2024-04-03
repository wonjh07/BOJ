import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

ans = 0
end = 0
N = int(input().rstrip())
conf = [tuple(map(int, input().rstrip().split(' '))) for _ in range(N)]
conf.sort(key = lambda x: x[0])
conf.sort(key = lambda x: x[1])

for i in range(len(conf)):
    if end <= conf[i][0]:
        ans += 1
        end = conf[i][1]

print(conf)
print(ans)
