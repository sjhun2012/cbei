a = int(input())

numbers = map(int, input().split())
    

b = int(input())
c = 0
for i in numbers:
    if i == b:
        c+=1
print(c)