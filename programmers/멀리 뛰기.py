
def solution(n):
    answer = 0
    li = [i +1  for i in range(n+1)]
    for i in range(2, n) :
        li[i] = li[i-1] + li[i-2]
    answer = li[n-1] % 1234567
    return answer