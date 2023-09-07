'''
getHeight 함수를 작성하세요.
'''


def getHeight(myTree):
    '''
    myTree의 높이를 반환하는 함수를 작성하세요.
    '''
    # ans = 1
    # if myTree.right == None and myTree.left == None :
    #     return 1
    # else :
    #     lHeight = 0
    #     rHeight = 0
    #     if myTree.left != None :
    #         lHeight = getHeight(myTree.left)

    #     if myTree.right != None :
    #         rHeight = getHeight(myTree.right)
    #     ans += max(lHeight, rHeight)
    if myTree == None:
        return 0
    else:
        return 1 + max(getHeight(myTree.left), getHeight(myTree.right))
    return ans