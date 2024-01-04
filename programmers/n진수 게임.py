import string

tmp = string.digits+string.ascii_uppercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p) :
    li = []
    for i in range(t * m) :
        li.append(convert(i, n))
    nums = "".join(li)
    ans = []
    for i in range(p-1, len(nums), m) :
        ans.append(nums[i])
        if len(ans) >= t : break
    print(ans)