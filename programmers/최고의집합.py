def solution(n, s):
    answer = []
    if s < n: return [-1]
    if s % n == 0:
        for i in range(n):
            answer.append(s // n)
    else:
        answer = [s // n for i in range(n)]
        print(answer)
        while True:
            sumAns = sum(answer)
            print(answer)
            if sumAns == s:
                break
            elif sumAns > s :
                for i in range(sumAns - s) :
                    answer[i%len(answer)] -= 1
            elif sumAns < s :
                for i in range(s - sumAns) :
                    answer[(i%len(answer))] += 1
    answer.sort()
    return answer

print(solution(2,9))

