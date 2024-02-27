a,b=map(int, input().split())
numbers = [0]*(a+1)
for i in range(a+1):
    numbers[i] = i
g=0
for i in range(b):
    c,d = map(int, input().split())
    g = numbers[c]
    numbers[c] = numbers[d]
    numbers[d] = g
for i in range(1, a+1):
    print(numbers[i],end = ' ')
