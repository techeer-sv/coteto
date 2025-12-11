def solution(genres, plays):
    d = {}
    # 장르별로 저장을 할 때 첫 번째 인덱스에는 각 곡의 합, 두 번째에는 각 곡의 인덱스와 재생수를 저장한다.
    for idx, genres in enumerate(genres):
        if genres not in d:
            d[genres] = [plays[idx], [plays[idx], idx]]
        else:
            d[genres][0] += plays[idx]
            d[genres].append([plays[idx], idx])
    # 정렬을 할 때는 .items필드를 활용해서 각 곡의 합 수에 맞게 정렬을 한다.
    sort_genres = sorted(d.items(), key=lambda item: item[1][0], reverse=True)
    # 그리고 결과에 맞게 출력한다.
    result = []
    for i in sort_genres:
        tmp = sorted(i[1][1:], key=lambda a: a[0], reverse=True)
        for score, idx in tmp[:2]:
            result.append(idx)
    return result


genres = ["classic", "a", "classic", "classic", "a", "a"]
plays = [500, 600, 150, 800, 2500, 600]

print(solution(genres, plays))
