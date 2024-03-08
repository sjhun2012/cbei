a=0
a = int(input())
b = [0] * a
b = list(map(int, input().split()))
c = b[0]
for i in range(a):
    if c < b[i]:
        c = b[i]
for i in range(a):
    b[i] = b[i]/c*100
d=0
for i in range(a):
    d+=b[i]
print(d/a)