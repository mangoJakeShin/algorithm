
from collections import deque
def solution(s):
    answer = True
    if (len(s) % 2 != 0) : return False
    bc = 0
    que =deque(s)
    while que :
        si = que.popleft()
        # print(s[i], bc)
        if si == "(" :
            bc += 1
        else :
            bc -= 1
        if bc < 0:
            return False

    if bc != 0 :
        answer = False

    return answer


from collections import deque


def solution(s):
    answer = True
    if len(s) % 2 != 0: return False
    li = []
    que = deque(s)
    for q in que:
        if q == ")":
            if len(li) < 1:
                return False
            else:
                li.pop(-1)
        else:
            li.append(1)
    if len(li) != 0: return False
    return answer