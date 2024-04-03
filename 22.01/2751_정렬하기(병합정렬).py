import sys
n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for i in range(n)]

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    l_arr = merge_sort(arr[:len(arr) // 2])
    r_arr = merge_sort(arr[len(arr) // 2:])

    mg_arr = []
    l = r = 0
    while l < len(l_arr) and r < len(r_arr):
        if l_arr[l] < r_arr[r]:
            mg_arr.append(l_arr[l])
            l += 1
        else:
            mg_arr.append(r_arr[r])
            r += 1
    mg_arr += l_arr[l:]
    mg_arr += r_arr[r:]
    return mg_arr

for i in merge_sort(arr):
	print(i)