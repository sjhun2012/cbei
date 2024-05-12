import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    res = 0
    l, r = arr[0], arr[0]
    for i in range(1, n):
        if l < r:
            res = max(res, arr[i]-l)
            l = arr[i]
        else:
            res = max(res, arr[i]-r)
            r = arr[i]
    res = max(res, arr[n-1] - l)
    res = max(res, arr[n-1] - r)
    print(res)