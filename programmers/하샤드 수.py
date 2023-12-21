def solution(x):
    s = list(str(x))
    for i in range(len(s)) :
        s[i] = int(s[i])
    return True if x % sum(s) == 0 else False