import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def t_counter(num):
    count_t = 0
    while num:
        num //= 2
        count_t += num
    return count_t

def f_counter(num):
    count_f = 0
    while num:
        num //= 5
        count_f += num
    return count_f

result_a = t_counter(n) - t_counter(m) - t_counter(n-m)
result_b = f_counter(n) - f_counter(m) - f_counter(n-m)
print(min(result_a, result_b))