'''
함수 find_order를 구현하세요.
'''


def find_order(p):
    '''
    괄호 p가 주어질 때, 각 괄호가 몇 번째로 계산되어야 하는 괄호인지를 list로 반환합니다.

    예를 들어, p='(()())' 일 경우, [3, 1, 1, 2, 2, 3] 을 반환합니다.
    '''
    idx = 0
    ord = 0
    stack = []
    ret = [1 for i in range(len(p))]
    for paren in p:
        if paren == "(":
            stack.append(idx)
            idx += 1
        else:

            ret[stack.pop(-1)] += ord
            ret[idx] += ord
            idx += 1
            ord += 1

    return ret