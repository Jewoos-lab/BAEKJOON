# 9506

while True:
    N = int(input())
    if N == -1:
        break
    A = []
    for i in range(1, N):
        if N % i == 0:
            A.append(i)

    if sum(A) == N:
        print(f"{N} = 1", end="")
        #print(N, " = ", " + ".join(str(i) for i in A), sep="")
        for j in range(1,len(A)):
            print(f" + {A[j]}", end="")
    else:
        print(N, "is NOT perfect.")

