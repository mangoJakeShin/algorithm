def solution(s) :
    answer = [0, 0]

    while len(s) >= 2:
        answer[1] += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        answer[0] += 1
        # if s == "1" : break
    return answer