def solution(n, words):
    answer = []
    used = []
    idx = 0
    last = words[0][0]
    times = [0 for k in range(n)]
    # 끝말잇기 탈락 인덱스 선정
    for i in range(len(words)):
        # 같은 말을 할때
        if words[i] in used:
            idx = i
            times[i % n] += 1
            break
        # 끝말이 아닐 때
        if words[i][0] != last:
            idx = i
            times[i % n] += 1
            break
        last = words[i][-1]
        times[i % n] += 1
        used.append(words[i])
    # 탈락자가 없을 때
    if idx == 0:
        return [0, 0]

    answer.append((idx % n) + 1)
    answer.append(times[idx % n])

    return answer