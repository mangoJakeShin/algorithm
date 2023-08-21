def solution(s) :
    answer = 0
    stack = []
    for i in range(len(s)) :
        if not stack :
            stack.append(s[i])
        else :
            now = stack.pop(-1)
            if s[i] == now :
                continue
            else :
                stack.append(now)
                stack.append(s[i])

    if not stack :
        answer = 1
    return answer