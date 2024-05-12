import sys
n,m = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

arr = [[0 for _ in range(m+2)] for _ in range(n+2)]
for i in range(n+2):
    arr[i][0] = -1
    arr[i][m+1] = -1
for j in range(m+2):
    arr[0][j] = -1
    arr[n+1][j] = -1

direct = [[0, 1], [1, 0], [0,-1], [-1,0]]
i=0
x, y = 1,0
now = 1
if(k > n * m):
    print(0)
else:
    while now <= k:
        x, y = x+direct[i][0], y+direct[i][1]
        arr[x][y] = now
        now+=1
        nx,ny = x+direct[i][0], y+direct[i][1]
        if arr[nx][ny] != 0:
            i = (i+1) % 4
    print(x,y)