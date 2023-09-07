'''
preorder, inorder, postorder 함수를 구현하세요.
'''


def preorder(tree):
    '''
    tree를 전위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''

    result = []
    result.append(tree.index)
    if tree.left != None:
        result += preorder(tree.left)
    if tree.right != None:
        result += preorder(tree.right)

    return result


def inorder(tree):
    '''
    tree를 중위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []

    if tree.left != None:
        result += inorder(tree.left)
    result.append(tree.index)

    if tree.right != None:
        result += inorder(tree.right)
    return result


def postorder(tree):
    '''
    tree를 후위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    if tree.left != None:
        result += postorder(tree.left)

    if tree.right != None:
        result += postorder(tree.right)
    result.append(tree.index)

    return result