'''
함수 processOrder를 구현하세요.
'''

'''
Queue 클래스를 구현하세요.
'''


class Queue:
    myQ = None

    def __init__(self):
        '''
        큐 myQueue을 만듭니다.
        '''
        self.myQ = []

    def push(self, n):
        '''
        queue에 정수 n을 넣습니다.
        '''
        self.myQ.append(n)

    def pop(self):
        '''
        queue에서 가장 앞에 있는 정수를 제거합니다. 만약 queue에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다.
        '''
        if len(self.myQ) > 0:
            return self.myQ.pop(0)

    def size(self):
        '''
        queue에 들어 있는 정수의 개수를 return 합니다.
        '''
        return len(self.myQ)

    def empty(self):
        '''
        queue이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        return 0 if len(self.myQ) > 0 else 1

    def front(self):
        '''
        queue의 가장 앞에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        return self.myQ[0] if len(self.myQ) > 0 else -1

    def back(self):
        '''
        queue의 가장 뒤에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        return self.myQ[-1] if len(self.myQ) > 0 else -1


class orderInfo:
    '''
    이 부분은 수정하지 마세요.
    '''

    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v


def processOrder(orders):
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 반환합니다.
    '''
    result = []
    tot = len(orders)
    q = Queue()
    vip = Queue()
    end = 0
    now = -1

    for i in range(len(orders)):
        now = orders[i].time
        if orders[i].vip == 0:
            q.push(i)
        else:
            vip.push(i)
        while end <= now and not (q.empty() == 1 and vip.empty() == 1):
            tq = selectQ(q, vip, end, orders)
            index = tq.front()
            end = max(end, orders[index].time) + orders[index].duration
            result.append(index + 1)
            tq.pop()
    while not (q.empty() == 1 and vip.empty() == 1):
        tq = selectQ(q, vip, end, orders)
        index = tq.front()
        end = max(end, orders[index].time) + orders[index].duration
        result.append(index + 1)
        tq.pop()

    return result


def selectQ(q, vip, end, orders):
    idx = q.front()
    vidx = vip.front()
    if vidx == -1:
        return q
    if idx == -1:
        return vip

    if end < orders[idx].time and end < orders[vidx].time:
        if orders[vidx].time <= orders[idx].time:
            return vip
        else:
            return q
    if end >= orders[idx].time and end < orders[vidx].time:
        return q
    if end >= orders[vidx].time and end < orders[idx].time:
        return vip

    return vip
