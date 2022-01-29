def countingsort(A, B, k):
    C = []

    for i in range(k+1):
        C.append(0)

    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1

    for i in range(1,k+1):
        C[i] = C[i] + C[i - 1]

    for k in range(len(A) - 1, -1, -1):
        B[C[A[k]] - 1] = A[k]
        C[A[k]] = C[A[k]] - 1

if __name__ == "__main__":
    A = [2,5,3,0,2,3,0,3]
    B = [0,0,0,0,0,0,0,0]
    k = 5
    countingsort(A,B,k)
    print(B)
