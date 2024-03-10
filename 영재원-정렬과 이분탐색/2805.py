import sys
n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

l, r = 0, 1000000000
res = 0

while l <= r:
    mid = (l + r) // 2
    s = 0
    for i in arr:
        s += max(i-mid, 0)
    if s >= m:
        l = mid+1
        res = max(res, mid)
    else:
        r = mid-1

print(res)