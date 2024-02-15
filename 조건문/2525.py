a, b = input().split()
a = int(a)
b = int(b)
c = int(input())

a += (c - c % 60) / 60
b += c % 60
a = int(a)

if b >= 60:
    a += 1
    b -= 60
if a >= 24:
    a -= 24

print(int(a), b)