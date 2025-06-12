def solution(s):
    answer = []
    oldnum = -1
    endrange = len(s)
    for idx in range(endrange):
        past = s[idx]
        if past == oldnum:
            continue
        else:
            answer.append(s[idx])
        oldnum = s[idx]
    return answer

def solution(s):
    answer = []
    answer. append(s[0])
    for i in s :
        if answer[-1] == i : continue
        answer.append(i)
    return answer