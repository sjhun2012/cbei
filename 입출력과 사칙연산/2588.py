a=input()
b=input()
a = int(a)
b = int(b)
print(a * (b%100%10))
print(int(a * (((b%100)-(b%100%10))/10)))
print(int(a * (b-(b%100))/100))
print(a * b)