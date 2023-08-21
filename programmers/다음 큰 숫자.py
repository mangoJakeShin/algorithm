def solution(n):
    answer = 0
    now = n + 1
    for i in range(n + 1, 1000000) :
        if (bin(n)[2:].count("1") == bin(now)[2:].count("1")):
            return now
        else:
            now += 1