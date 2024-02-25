a=int(input())
numbers = list(map(int, input().split()))
c = numbers[0]
e = ""
for i in numbers:
    if c > i:
        c = i
e+=str(c)
e+=" "
c = numbers[0]
for i in numbers:
    if c < i:
        c = i
e+=str(c)
print(e)