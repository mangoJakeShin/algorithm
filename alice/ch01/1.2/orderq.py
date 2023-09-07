'''
함수 processOrder를 구현하세요.
'''

from queue import Queue

class orderInfo:
    '''
    이 부분은 수정하지 마세요.
    '''
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v

def processOrder(orders) :
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 반환합니다.
    '''
    result = []
    tot = len(orders)
    normalQueue = Queue()
    vip = Queue()
    end = 0
    curTime = -1


    for i in range(len(orders)) :
        curTime = orders[i].time
        if orders[i].vip == 0 :
            normalQueue.put(i)
        else :
            vip.put(i)
        while end <= curTime and not(normalQueue.empty() and vip.empty()):
            tq = selectQ(normalQueue, vip, end, orders)
            index = tq.queue[0]
            end = max(end, orders[index].time) + orders[index].duration
            result.append(index + 1)
            tq.get()
    while not(normalQueue.empty() and vip.empty()):
        tq = selectQ(normalQueue, vip, end, orders)
        index = tq.queue[0]
        end = max(end, orders[index].time) + orders[index].duration
        result.append(index + 1)
        tq.get()


    return result

def selectQ(q, vip, end, orders) :
    idx = -1 if len(q.queue) == 0 else q.queue[0]
    vidx = -1 if len(vip.queue) == 0 else vip.queue[0]
    if vidx == -1 :
        return q
    if idx == -1 :
        return vip

    if end < orders[idx].time and end < orders[vidx].time:
        if orders[vidx].time <= orders[idx].time :
            return vip
        else :
            return q
    if end >= orders[idx].time and end < orders[vidx].time :
        return q
    if end >= orders[vidx].time and end < orders[idx].time :
        return vip

    return vip
