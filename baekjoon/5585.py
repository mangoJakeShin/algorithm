def solution(money) :
    answer = 0
    li = [500,100,50,10,5,1]
    money = 1000 - money
    for l in li :
        ch, money = change(money,l)
        answer += ch
    return answer

def change(inp,oup ) :
    return [inp//oup, inp%oup]

# s = int(input())
# print(solution(s))

def sol(x,y) :
# x = int(input())
# y = int(input())

    if x >= 0:
        print(4 if y > 0 else 2)
    return 1
import re
a = "1 4 1 2 4 2 4 2 3 4 4"
s = a.split(" ").count('2')
print(s)