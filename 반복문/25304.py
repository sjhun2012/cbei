a = int(input())
b = int(input())
count = 0
for i in range(b):
    c,d=input().split()
    c=int(c)
    d=int(d)
    count+=c*d
if(count == a):
    print("Yes")
else:
    print("No")
