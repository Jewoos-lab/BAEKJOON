# 11557번

T = int(input())
for _ in range(T):
    N = int(input())
    dic = {}
    for _ in range(N):
        a, b = input().split()
        dic[b] = a
    max = 0
    for i in dic:
        i = int(i)
        if max < i:
            max = i
    print(dic[str(max)])


