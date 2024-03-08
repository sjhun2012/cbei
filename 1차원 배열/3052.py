a = [1] * 42

b=0
for i in range(10):
    b = int(input())
    a[b%42] = 0
c=0
for i in range(42):
    if a[i] == 0:
        c+=1
print(c)
