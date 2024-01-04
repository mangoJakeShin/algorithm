def solution(n):
    answer = 0
    li = [i + 1 for i in range (int(n/2 + 1))]
    added = 0
    for i in range(len(li)) :
        print("==", i, answer)
        for j in range(i, len(li)) :
            print(j, added)
            if added > n :
                added  = 0
                break
            elif added == n :
                answer += 1
                added = 0
                break
            else :
                added += li[j]

    print(answer)
    return answer

solution(15)
