'''
1. LinkedListPipe 클래스를 완성하세요.
2. procesBeads 함수를 완성하세요.
'''


class LinkedListElement:
    def __init__(self, val, ptr):
        self.value = val
        self.myNext = ptr


class LinkedListPipe:
    '''
    Linked List를 이용하여 다음의 method들을 작성하세요.
    '''

    def __init__(self):
        '''
        리스트 myPipe를 만듭니다. 이는 구슬의 배치를 저장합니다.
        '''
        self.start = None
        self.end = None

    def addLeft(self, n):
        if self.start == None :
            bid = LinkedListElement(n, None)
            self.start = bid
            self.end = bid
        else :
            self.start = LinkedListElement(n, self.start)
    def addRight(self, n):
        if self.start == None :
            bid = LinkedListElement(n, None)
            self.start = bid
            self.end = bid
        else :
            curBid = self.end
            newBid = LinkedListElement(n, None)
            curBid.myNext = newBid
            self.end = newBid


    def getBeads(self):
        '''
        파이프의 배치를 list로 반환합니다.
        '''
        retList = []
        curBid = self.start
        while curBid.myNext != None :
            retList.append(curBid.value)
            curBid = curBid.myNext
        retList.append(curBid.value)
        return retList

def processBeads(myInput):
    '''
    구슬을 파이프에 넣는 행위가 myInput으로 주어질 때, 구슬의 최종 배치를 리스트로 반환하는 함수를 작성하세요.

    myInput[i][0] : i번째에 넣는 구슬의 번호
    myInput[i][1] : i번째에 넣는 방향

    예를 들어, 예제의 경우

    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0

    입니다.

    '''

    myPipe = LinkedListPipe()
    for input in myInput :
        bidNum, dir  = input[0], input[1]
        if dir == 0 :
            myPipe.addLeft(bidNum)
        else : myPipe.addRight(bidNum)
    result = myPipe.getBeads()

    return result