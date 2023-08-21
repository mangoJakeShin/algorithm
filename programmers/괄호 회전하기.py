def solution(s) :
    answer = 0
    for i in range(len(s)) :
        if bracket(s) :
            answer += 1
        s = s[1:] + s[0]
    return answer


def bracket(br) :
    pair = {"}": "{", ")": "(", "]": "["}
    keys = pair.keys()
    stack = []
    for i in range(len(br)) :
        if br[i] in keys and stack:
            if stack.pop(-1) == pair[br[i]] :
                continue
            else:
                return False
        elif br[i] not in keys :
            stack.append(br[i])
        else :
            return False
    return True if len(stack) == 0 else False