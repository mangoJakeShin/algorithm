def solution(n) :
    dx = [0,1-1]
    dy = [1,0,-1]
    maxn = n
    minn = 0
    li = [i for i in range(1, n+1)]
    sumli = sum(li)
    final = [0 for i in range(sumli + 1)]
    cur = [0,0]
    dir = 0
    for i in range(1,sumli) :
        final[sum(li[:cur[0]]) + cur[1]] = i
        if cur[0] < minn :
            pass

solution(6)