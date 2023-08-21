def solution(brown, yellow):
    answer = []
    total = brown + yellow

    for idx in range(1,brown+1):
        rowexpect = total // idx
        leftover = total % idx
        checker = idx * rowexpect

        if (leftover == 0 and (checker == total) and ( total > (rowexpect + idx))):
            row = rowexpect
            column = idx
            if (( (row-2) * (column-2) == yellow) and ( row >= column)):
                answer.append(row)
                answer.append(column)


    return answer