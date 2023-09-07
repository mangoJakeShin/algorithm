'''
orderManager 클래스를 완성하세요.
'''

class orderManager :
    '''
    주문을 처리하는 class를 작성합니다.
    '''

    def __init__(self) :
        '''
        이 부분은 고치지 마세요.
        '''
        self.data = []

    def addOrder(self, orderId) :
        self.data.append(orderId)

    def removeOrder(self, orderId) :
        self.data.remove(orderId)

    def getOrder(self, orderId) :
        idx = -1
        if orderId in self.data :
            idx = self.data.index(orderId) + 1
        return idx