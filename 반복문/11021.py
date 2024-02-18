a = int(input())
c="Case #"
for i in range(a):
    a,b=input().split()
    a=int(a)
    b=int(b)
    print(f'Case #{i+1}{":"}', a+b)