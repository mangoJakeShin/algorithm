'''
Stack 클래스를 완성하세요.
'''


class Stack:
    myStack = None
    '''
    List를 이용하여 다음의 method들을 작성하세요.
    '''

    def __init__(self):
        self.myStack = []

    def push(self, n):
        self.myStack.append(n)

    def pop(self):
        if len(self.myStack) > 0:
            return self.myStack.pop(-1)

    def size(self):
        return len(self.myStack)

    def empty(self):
        '''
        stack이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        print("@@@@", len(self.myStack))
        return 0 if len(self.myStack) > 0 else 1

    def top(self):
        '''
        stack의 가장 위에 있는 정수를 return 합니다. 만약 stack에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''

        return self.myStack[-1] if len(self.myStack) > 0 else -1
