def solution(s):
    answer = ''
    n = s.split(" ")
    nums = []
    for num in n :
        nums.append(int(num))
    answer += str(min(nums)) + " " + str(max(nums))
    return answer