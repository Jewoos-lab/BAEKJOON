# 10162
A = 300
B = 60
C = 10

T = int(input())

if T % 10 != 0:
    print(-1)
else:
    x = T // A
    y = T % A // B
    z = T % A % B // C

    print(x,y,z)