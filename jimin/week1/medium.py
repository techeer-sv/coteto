def solution(clothes):
    counts = {}
    for name, kind in clothes:
        counts[kind] = counts.get(kind, 0) + 1

    ans = 1
    for kind in counts:
        ans *= (counts[kind] + 1)  # 그 종류에서 (입는 경우 수 + 안 입는 경우 1)

    return ans - 1  # 아무것도 안 입는 경우 제외
