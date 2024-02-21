a,b = input().split()
a=int(a)
b=int(b)
numbers = map(int, input().split())
f=""
g=0
for i in numbers:
    if i < b:
        if(g == 0):
            g=1
        else:
            f+=" "
        f+=str(i)
print(f)