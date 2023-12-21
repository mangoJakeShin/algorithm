def solution(n):
    answer = 0
    s = list(str(n))
    s.sort(reverse=True)
    return int("".join(s))