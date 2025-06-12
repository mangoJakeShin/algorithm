# def solution(n):
#     answer = ''
#     return answer
#
# 1	1 - 1
# 2	2 - 2
# 3	4 - 3
# 4	11 1 1 - 1 1
# 5	12 1 2 - 1 2
# 6	14 2 0 - 1 3
# 7	21 2 1 - 2 1
# 8	22 2 2 - 2 2
# 9	24 3 0 - 2 3
# 10    41 3 1 - 3 1
# 11    42 3 2 - 3 2
# 12    44 4 0 - 3 3
# 13    111 4 1 - 1 1 1
# 14    112 4 2 - 1 1 2
# 15    114 5 0 - 1 2 0 - 1 1 3
# 16    121 5 1 - 1 2 1 - 1 2 1
# 17    122 5 2 - 1 2 2 - 1 2 2
# 18    124 6 0 - 2 0 0 - 1 3 0 - 1 2 3
# 19    141 6 1 - 2 0 1 - 1 3 1
# 20    142 6 2 - 2 0 2 - 1 3 2

def div(n, l) :
    print(n, l)
    if n > 3 :
        if n//3 > 3 :
            l += div(n//3, [])
        else :
            l.append(n//3)
        return div(n % 3, l)
    else :
        l.append(n)
        return l

li = div(20,[])
print(li)
ls = [1,2,4]
a = ""
for i in range(len(li)-1) :
    print("@@@",ls[(li[i])-1])
    a += str(ls[(li[i])-1])
print(li[-1])
a += str(ls[li[-1]])
print(a)
