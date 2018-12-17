def fourSumCount(A, B, C, D):
    tmp1 = []
    n = len(A)
    for i in range(n):
        for j in range(n):
            tmp1.append(A[i] + B[j])
    tmp2 = []
    for i in range(n):
        for j in range(n):
            tmp2.append(C[i] + D[j])
    i, j = 0, len(tmp2) - 1
    tmp1.sort()
    tmp2.sort()
    ans = 0
    while i < len(tmp1) and j >= 0:
        tmp = tmp1[i] + tmp2[j]
        if tmp == 0:
            ans += 1
            i += 1
            j -= 1
        elif tmp < 0:
            i += 1
        else:
            j -= 1
    print ans
    return ans
if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    fourSumCount(A,B,C,D)