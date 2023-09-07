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

    def addOrder(self, orderId):
        newOrd = LinkedListElement(orderId, None, None)
        if self.start == None and self.end == None:
            self.start = newOrd
            self.end = newOrd
        else:
            self.end.myNext = newOrd
            newOrd.myPrev = self.end
            self.end = newOrd

    def removeOrder(self, orderId):
        if self.start == None and self.end == None:
            return

        curBid = self.start
        if curBid.data == orderId and curBid.myPrev == None and curBid.myNext == None:
            self.start = None
            self.end = None
            return
        while curBid != None:
            if curBid.data == orderId:
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
            curBid = curBid.myNext

    def getOrder(self, orderId):
        curBid = self.start
        ret = 1  # 초기 값을 1로 설정
        while curBid != None:
            if curBid.data == orderId:
                return ret
            ret += 1
            curBid = curBid.myNext
        return -1
