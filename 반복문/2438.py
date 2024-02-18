a = int(input())
b=""
e=""
for i in range(a):
    for c in range(a-i-1):
        b+=" "

    for j in range(i+1):
        b+="*"
    print(b)
    b=""
    e=""