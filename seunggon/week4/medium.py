def solution(answers):
    
    scores = [0,0,0]
    
    methods = [[1,2,3,4,5], [2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    
    for i, answer in enumerate(answers):
            for idx, method in enumerate(methods): # N번 반복 아님
                # 패턴의 길이가 다 달라서 문제 개수에 나머지 연산
                if method[i % len(method)] == answer:
                    scores[idx] += 1      
    
    max_score = max(scores)

    answer = []

    # scores 리스트를 다 탐색해야 중복도 append 가능
    for i, score in enumerate(scores):
        if score == max_score:
            answer.append(i + 1)
    
    
    return answer