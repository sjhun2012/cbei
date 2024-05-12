import sys

def time_to_min(a):
    return int(a[:2]) * 60 + int(a[2:])
arr = []
n = int(sys.stdin.readline())
for i in range(n):
    s, e = sys.stdin.readline().split()
    s, e = time_to_min(s) - 10, time_to_min(e) + 10
    arr.append((s, e))
arr.append((-10, time_to_min('1000')))
arr.append((time_to_min('2200'), 2000))
arr = sorted(arr)
res, max_e=0,0
for s, e in arr:
    res = max(res, s-max_e)
    max_e = max(max_e, e)
print(res)