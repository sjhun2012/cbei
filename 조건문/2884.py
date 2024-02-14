a, b = input().split()
a = int(a)
b = int(b)

if b < 45 :	# 분단위가 45분보다 작을 때 
    if a == 0 :	# 0 시이면
        a = 23
        b += 60
    else :	# 0시가 아니면 (0시보다 크면)
        a -= 1	
        b += 60
        
print(a, b-45)	