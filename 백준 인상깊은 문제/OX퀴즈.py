# 8958번
N = int(input())



for i in range(N):
    ox = list(input())
    score = 0
    sum = 0
    for j in ox:
        if j == "O":
            score += 1
        else:
            score = 0
        sum += score
    print(sum)