a = int(input())
b = "" 
for i in range(int((a-a%4)/4-1)):
    b+="long "
b+="long"
print(b, "int")