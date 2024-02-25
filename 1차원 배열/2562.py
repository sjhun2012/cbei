a=0
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(9):
    a = int(input())
    numbers[i] = a
    b=numbers[0]
e=0
d=0
for i in numbers:
    if(i > b):
        b=i
        e=d
    d+=1
print(b)
print(e+1)