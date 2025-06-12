def solution(k, tangerine):
    answer = 0
    tans = {}

    for i in range(len(tangerine)):
        if tangerine[i] not in tans.keys() :
            tans[tangerine[i]] = 1
        else :
            tans[tangerine[i]] += 1
    tan1 = sorted(tans.items(), key = lambda x : -x[1])
    sums = 0
    while(sums < k) :
        sums += tan1.pop(0)[1]
        answer += 1

    return answer2

