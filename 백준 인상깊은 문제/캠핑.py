# 4796번

i = 1

while True:
    L, P, V = map(int, input().split())

    if L + V + P == 0:
        break

    result = (V//P * L) + min(V % P, L)
    print(f"Case {i}: {result}")
    i += 1