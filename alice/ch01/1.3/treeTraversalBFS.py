'''
BFS 함수를 구현하세요.
'''

def BFS(tree) :
    '''
    tree를 너비 우선 탐색으로 순회하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    q =[]
    q.append(tree)
    while len(q) != 0 :
        result.append(q[0].index)
        if q[0].left != None :
            q.append(q[0].left)
        if q[0].right != None :
            q.append(q[0].right)
        q.pop(0)

    return result