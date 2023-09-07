'''
1. LinkedListElement 클래스를 완성하세요.
2. orderManager 클래스를 완성하세요.
'''


class LinkedListElement:
    def __init__(self, data, myPrev, myNext):
        self.data = data
        self.myPrev = myPrev
        self.myNext = myNext


class orderManager:
    def __init__(self):
        self.start = None
        self.end = None
        self.li = {}

    def addOrder(self, orderId):

        if self.start == None and self.end == None:
            newOrd = LinkedListElement(orderId, None, None)
            self.start = newOrd
            self.end = newOrd
        else:
            newOrd = LinkedListElement(orderId, self.end, None)
            self.end.myNext = newOrd
            self.end = newOrd
        self.li[orderId] = newOrd

    def removeOrder(self, orderId):

        if self.start == None and self.end == None:
            return

        curBid = self.li[orderId]
        pre = curBid.myPrev
        nex = curBid.myNext

        if pre != None:
            pre.myNext = nex

        if nex != None:
            nex.myPrev = pre
        if curBid == self.end:
            self.end = pre
        if curBid == self.start:
            self.start = nex

    def getOrder(self, orderId):
        curBid = self.start
        ret = 1  # 초기 값을 1로 설정
        while curBid != None:
            if curBid.data == orderId:
                return ret
            else:
                ret += 1
                curBid = curBid.myNext
        return -1
