def solution(A,B):
    sum = 0
    
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        sum = sum + A[i]*B[i]

    return sum