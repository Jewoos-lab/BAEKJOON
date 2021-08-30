# 11653번

S = int(input())

n = 1

# n*(n+1)/2는 1~n까지의 합 공식
while n*(n+1)/2 <= S:
    n += 1
print(n-1)