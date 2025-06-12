import math
def solution(progresses, speeds):
    answer = []
    temp = []
    for i in range(len(progresses)):
        days = math.ceil((100-progresses.pop()) / speeds.pop())
        temp.append(days)
    max = temp.pop()
    days = 1
    while(len(temp)):
        num = temp.pop()

        if num > max:
            answer.append(days)
            days = 1
            max = num
        else:
            days += 1
    answer.append(days)
    return answer

print(math.ceil((100 - 30) / 30))

import math


def solution(progresses, speeds):
    answer = []
    n = 0
    for i range(len(progresses)):
        if progresses[i] + (speeds[i] * n) < 100:
            n = math.ceil((100 - progresses[i]) / speeds[i])
            answer.append(1)
        else:
            answer[-1] += 1

    return answer