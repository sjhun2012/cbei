import sys

n=int(sys.stdin.readline())
arr = [0 for i in range(10001)]

for i in range(n):
    a = int(sys.stdin.readline())
    arr[a] += 1

for i in range(10001):
    for j in range(arr[i]):
        print(i)
