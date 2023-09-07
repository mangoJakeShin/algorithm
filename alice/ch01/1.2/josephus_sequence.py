'''
josephus_sequence 함수를 작성하세요.
'''

def josephus_sequence(n, k) :
    ret = []
    fst = 0
    q = [i + 1 for i in range(n)]
    print(q)
    for i in range(n) :
        for j in range(k - 1) :
            q.append(q.pop(0))
        ret.append(q.pop(0))

    return ret