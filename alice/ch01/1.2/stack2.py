'''
CheckParen 함수를 완성하세요.
단, Stack 클래스를 사용하세요.
'''


class Stack:
    '''
    이전 실습에서 작성한 Stack 클래스 코드를 사용합니다.
    '''

    myStack = None

    def __init__(self):
        '''
        자료를 저장할 공간(리스트) myStack을 만듭니다.
        '''
        self.myStack = []

    def push(self, n):
        '''
        stack에 정수 n을 넣습니다.
        '''
        self.myStack.append(n)

    def pop(self):
        '''
        stack에서 가장 위에 있는 정수를 제거합니다. 만약 stack에 아무 원소가 없다면 아무 일도 하지 않습니다.
        '''
        if len(self.myStack) > 0:
            return self.myStack.pop(-1)

    def size(self):
        '''
        stack에 들어 있는 정수의 개수를 return 합니다.
        '''
        return len(self.myStack)

    def empty(self):
        '''
        stack이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        return 0 if len(self.myStack) > 0 else 1

    def top(self):
        '''
        stack의 가장 위에 있는 정수를 return 합니다. 만약 stack에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''

        return self.myStack[-1] if len(self.myStack) > 0 else -1


def checkParen(p):
    '''
    괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환
    '''
    st = Stack()
    for par in p:
        if par == ")":
            if st.empty() == 1 or st.top() != "(":
                return "NO"
            else:
                st.pop()
        else:
            st.push(par)

    return "YES" if st.empty() == 1 else "NO"