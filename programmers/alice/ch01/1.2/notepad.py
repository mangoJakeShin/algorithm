'''
notepad 함수를 작성하세요.
'''

def notepad(s, commands) :
    stack = list(s)
    tmp = []

    for com in commands :
        command = com.split()
        act = command[0]
        if act == "L" and len(stack) > 0 :
            tmp.append(stack.pop())
        elif act == "R" and len(tmp) > 0 :
            stack.append(tmp.pop())
        elif act == "D" and len(stack) > 0 :
            stack.pop()
        elif act == "P" :
            stack.append(command[1])
    ans = stack + tmp[::-1]
    ret = ""
    for i in range(len(ans)) :
        ret += ans[i]
    return ret