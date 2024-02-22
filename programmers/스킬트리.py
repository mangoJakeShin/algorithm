def solution(skill, skill_trees):
    answer = 0
    for skill_list in skill_trees:
        i = 0
        for skills in skill_list:
            # 선행스킬 목록에 있다면?
            if skills in skill:
                if skill[i] != skills:
                    break
                else:
                    i += 1
                # 지금 아닌 경우 실패
                if skills == skill_list[-1] :
                    answer += 1
            else:
                if  i == len(skill) :
                    answer += 1
                    break

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))