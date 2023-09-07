'''
is_stack_sequence 함수를 작성하세요.
'''

def is_stack_sequence(nums) :
    stack = [1]
    cur = 0
    for i in range(2,len(nums) + 1) :
        while len(stack) > 0 and stack[-1] == nums[cur] :
            stack.pop()
            cur = cur + 1
        if len(stack) == 0 or stack[-1] < nums[cur] :
            stack.append(i)
        else :
            return "No"
    return "Yes"