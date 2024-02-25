a=0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,22,23,24,25,26,27,28,29,30]
number = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(28):
    a = int(input())
    number[i] = a
d=0
e=0
for i in number:
    d=0
    for j in numbers:
        if j == i:
            numbers[d] = 0
        d+=1
for i in numbers:
    if i != 0:
        print(i)