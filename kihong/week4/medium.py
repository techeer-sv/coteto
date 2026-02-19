def solution(answers):

    # 각 입력 값 루틴 입력
    user = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    }
    # 확인하고자 하는 인덱스 선언
    idx = 0
    # 각 인덱스 별 idx와 num 선언
    result = [[0, 0], [1, 0], [2, 0], [3, 0]]
    while idx < len(answers):
        if user[1][idx % 5] == answers[idx]:
            result[1][1] += 1
        if user[2][idx % 8] == answers[idx]:
            result[2][1] += 1
        if user[3][idx % 10] == answers[idx]:
            result[3][1] += 1
        idx += 1
    answer = []
    max_num = 0
    # 입력된 idx와 num을 토대로 greedy 형태로 answer  업데이트
    for idx, num in result[1:]:
        if not answer:
            answer.append(idx)
            max_num = num
        else:
            if max_num < num:
                max_num = num
                answer = [idx]
            elif max_num == num:
                answer.append(idx)

    return answer


inputs = [[1, 2, 3, 4, 5], [1, 3, 2, 4, 2]]

for input in inputs:
    print(solution(input))  # [1], [1,2,3]
