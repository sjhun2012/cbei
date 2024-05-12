n=0
n = int(input())
start = [0] * n
finish = [0] * n
for i in range(n):
    start[i] = int(input())
    finish[i] = int(input())
h=0
if (start[0])%100 > 10:
    h+=start[0]%100
for i in range(n):
    if(finish[i]%100)