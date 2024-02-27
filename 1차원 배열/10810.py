a,b=map(int, input().split())
numbers = [0]*(a+1)
for i in range(b):
    c,d,e = map(int, input().split())
    for j in range(c,d+1):
        numbers[j] = e
for i in range(1, a+1):
    print(numbers[i],end = ' ')
