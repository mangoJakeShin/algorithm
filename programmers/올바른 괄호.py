
from collections import deque
def solution(s):
    answer = True

    if (len(s) % 2 != 0) :
        return False
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