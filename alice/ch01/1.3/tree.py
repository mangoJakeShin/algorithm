class Tree:
    def __init__(self, i, l, r):
        self.index = i
        self.left = l
        self.right = r

    def addNode(self, i, l, r):
        '''
        트리 내의 정점 i에 대하여 왼쪽자식을 l, 오른쪽 자식을 r로
        설정해주는 함수를 작성하세요.
        '''
        l = l if l != None else -1
        r = r if r != None else -1
        if self.index == None or self.index == i:
            self.index = i
            self.left = Tree(l, None, None) if l != -1 else None
            self.right = Tree(r, None, None) if r != -1 else None
        else:
            flag = False

            if self.left != None:
                flag = self.left.addNode(i, l, r)
            if not flag and self.right != None:
                self.right.addNode(i, l, r)
            return flag