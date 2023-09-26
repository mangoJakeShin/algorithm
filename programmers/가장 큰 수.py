def solution(numbers):
    answer = ''
    numlist = quickSort(numbers)
    print(numlist)
    answer = str(int("".join(numlist)))
    return answer

def leftSort(numlist, pv):
    tmpli = []
    for i in range(len(numlist)):
        if compareStrNum(numlist[i], pv):
            tmpli.append(str(numlist[i]))
    return tmpli



def rightSort(numlist, pv):
    tmpli = []

    for i in range(len(numlist)):
        if not compareStrNum(numlist[i], pv) :
            tmpli.append(str(numlist[i]))

    return tmpli

def quickSort(array) :
    if len(array) <= 1:
        return array
    pivot = array[0]
    left = leftSort(array[1:], pivot)
    right = rightSort(array[1:], pivot)
    return quickSort(left) + [str(pivot)] + quickSort(right)

def compareStrNum(a, b) :
    a, b = str(a)[::-1], str(b)[::-1]
    while True :
        if a[-1] == b[-1] :
            if len(a) == 1 and len(b) == 1 :
                return True
            if len(a) > 1 : a = a[:-1]
            if len(b) > 1 : b = b[:-1]
        elif a[-1] > b[-1] :
            return True
        elif a[-1] < b[-1] :
            return False

print(solution([555, 565, 566, 55, 56, 5, 54, 544, 549]))

