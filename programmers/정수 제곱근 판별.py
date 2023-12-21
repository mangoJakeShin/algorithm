from math import sqrt
def solution(n):
    s = sqrt(n)
    return (s + 1) ** 2 if s == int(s) else -1