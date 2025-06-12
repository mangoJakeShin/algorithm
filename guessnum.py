import random

import itertools

# 사용 예시
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 33333
def guess(target)  :
    nums_str = [str(n) for n in nums]
    results = []

    # 가능한 모든 숫자 조합과 순열 생성
    for perm in itertools.permutations(nums_str, len(nums)):
        # xxxxx(5자리) - xxxx(4자리)로 나눔
        first_num = int(''.join(perm[:5]))
        second_num = int(''.join(perm[5:]))

        if first_num - second_num == target:
            results.append((first_num, second_num))

    return results  # 조합이 없을 경우 None 반환



print(guess(22222))



def find_target_combination(nums, target):
    nums_str = [str(n) for n in nums]

    # 가능한 모든 숫자 조합과 순열 생성
    for perm in itertools.permutations(nums_str, len(nums)):
        # xxxxx(5자리) - xxxx(4자리)로 나눔
        first_num = int(''.join(perm[:5]))
        second_num = int(''.join(perm[5:]))

        if first_num - second_num == target:
            return first_num, second_num

    return None  # 조합이 없을 경우 None 반환



result = find_target_combination(nums, target)

if result:
    print(f'{result[0]} - {result[1]} = {target}')
else:
    print('해당 target을 만족하는 조합이 없습니다.')
