def solution(genres, plays):
    d = {}
    sum = {}
    answer = []
    for i, val in enumerate(plays):
        genre = genres[i]
        if genre in d:
            d[genre].append([i,val])
            sum[genre] += val
        else:
            d[genre] = [[i,val]]
            sum[genre] = val
    genres_sorted = sorted(sum.items(), key=lambda x: x[1], reverse=True)
    for genre, _ in genres_sorted:
        sorted_plays = sorted(d[genre], key=lambda x: x[1], reverse=True)
        d[genre] = sorted_plays
        answer.extend([x[0] for x in d[genre][:2]])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))