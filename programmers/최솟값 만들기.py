def solution(A,B):
    A.sort()
    B = sorted(B, key=lambda x : (-x))
    answer = 0
    for i in range(len(A)) :
        answer += A[i] * B[i]

    return answer