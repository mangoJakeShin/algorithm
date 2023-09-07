'''
getWidth 함수를 작성하세요.
'''
'''
중위순회 함수를 만들어 모든 노드들을 일렬로 정렬시키면 각 노드의 열이 나온다. -> inorder
그 후 각 행(깊이)의 맨 왼쪽 값과 맨 오른쪽 값을 찾는다. -> left[d], right[d]
이후 각 깊이별로 가장 멀리 떨어진 노드끼리의 비교를 수행한다. -> ans, ansd
'''


def inorder(tree, depth):
    result = []
    if tree.left != None:
        result += inorder(tree.left, depth + 1)
    tree.setDepth(depth)
    result.append(tree)
    if tree.right != None:
        result += inorder(tree.right, depth + 1)
    return result


def getWidth(myTree):
    '''
    myTree의 너비가 가장 넓은 레벨과 그 레벨의 너비를 반환하는 함수를 작성하세요.
    가장 넓은 레벨 l과 그 레벨의 너비 w를 튜플로 반환해야 합니다.

    반환값 형식 : (l, w)
    '''
    result = inorder(myTree, 1)
    n = len(result)

    # left = 깊이가 i인 모든 노드들 중에서 가장 왼쪽노드의 행
    # right = 깊이가 i인 모든 노드들 중에서 가장 오른쪽 노드의 행
    # 어떤 깊이의 너비는 right[i] - left[i]
    left = [1001 for i in range(1001)]
    right = [-1 for i in range(1001)]
    maxDepth = 0

    for i in range(n):
        d = result[i].depth
        left[d] = min(left[d], i)
        right[d] = max(right[d], i)
        print(result[i].index, left[d], right[d], d, maxDepth)
        maxDepth = max(maxDepth, d)
    ansd = 0
    ans = 0

    for i in range(1, maxDepth + 1):
        print("@@", left[i], right[i])
        temp = right[i] - left[i] + 1
        if ans < temp:
            ansd = i
            ans = temp

    return (ansd, ans)