arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
ret1 = [[22, 22, 11], [36, 28, 18], [29, 20, 14]]

arr11 = [[1, 4], [3, 2], [4, 1]]
arr22 = [[3, 3], [3, 3]]
ret2 = [[15, 15], [15, 15], [15, 15]]

# ret = [[0 for i in range(len(arr1[0]))] for j in range(len(arr1))]
a = []
for arr in arr1:
    ret = []
    for j in range(len(arr2[0])):
        sum = 0
        for dy, num in enumerate(arr):
            print(sum, "+=", num, "*", "arr2",dy,"|", j)
            sum += num * arr2[dy][j]
        ret.append(sum)
        # for k in range(len(arr1[0])):
        #     arr[i][k] += arr1[i][j] * arr2[j][k]
    a.append(ret)
print(a)
