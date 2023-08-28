import string
import math

tmp = string.digits + string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, k):
    answer = 0
    conv = convert(n, k)
    conv = conv.split("0")
    prime = [2, 3]
    print(conv)
    for num in conv:
        if num != "":
            num = int(num)
            if num in prime:
                answer += 1
                continue
            for i in range(4, int(num**(1/2))+1):
                if num % i == 0:
                    break
                if i == num // 2 + 1:
                    answer += 1
                    prime.append(num)

    return answer

print(solution(524287,2))