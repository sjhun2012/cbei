b = input()
numbers = [1000] * 26
for i in range(len(b)):
        if b[i] == 'a':
            if numbers[0] == 1000:
                numbers[0] = i
        if b[i] == 'b':
            if numbers[1] == 1000:
                numbers[1] = i
        if b[i] == 'c':
            if numbers[2] == 1000:
                numbers[2] = i
        if b[i] == 'd':
            if numbers[3] == 1000:
                numbers[3] = i
        if b[i] == 'e':
            if numbers[4] == 1000:
                numbers[4] = i
        if b[i] == 'f':
            if numbers[5] == 1000:
                numbers[5] = i
        if b[i] == 'g':
            if numbers[6] == 1000:
                numbers[6] = i
        if b[i] == 'h':
            if numbers[7] == 1000:
                numbers[7] = i
        if b[i] == 'i':
            if numbers[8] == 1000:
                numbers[8] = i
        if b[i] == 'j':
            if numbers[9] == 1000:
                numbers[9] = i
        if b[i] == 'k':
            if numbers[10] == 1000:
                numbers[10] = i
        if b[i] == 'l':
            if numbers[11] == 1000:
                numbers[11] = i
        if b[i] == 'm':
            if numbers[12] == 1000:
                numbers[12] = i
        if b[i] == 'n':
            if numbers[13] == 1000:
                numbers[13] = i
        if b[i] == 'o':
            if numbers[14] == 1000:
                numbers[14] = i
        if b[i] == 'p':
            if numbers[15] == 1000:
                numbers[15] = i
        if b[i] == 'q':
            if numbers[16] == 1000:
                numbers[16] = i
        if b[i] == 'r':
            if numbers[17] == 1000:
                numbers[17] = i
        if b[i] == 's':
            if numbers[18] == 1000:
                numbers[18] = i
        if b[i] == 't':
            if numbers[19] == 1000:
                numbers[19] = i
        if b[i] == 'u':
            if numbers[20] == 1000:
                numbers[20] = i
        if b[i] == 'v':
            if numbers[21] == 1000:
                numbers[21] = i
        if b[i] == 'w':
            if numbers[22] == 1000:
                numbers[22] = i
        if b[i] == 'x':
            if numbers[23] == 1000:
                numbers[23] = i
        if b[i] == 'y':
            if numbers[24] == 1000:
                numbers[24] = i
        if b[i] == 'z':
            if numbers[25] == 1000:
                numbers[25] = i
for i in range(25):
    if numbers[i] == 1000:
        print("-1", end=" ")
    else:
        print(numbers[i], end=" ")
if numbers[25] == 1000:
    print("-1", end="")
else:
    print(numbers[25], end="")    