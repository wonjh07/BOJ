# A+ B -4
# 종료 조건이 없을때 빠져 나가게 해야

while True:
    try:
        a, b = map(int, input().split(' '))
        print(a + b)
    except:
        break
