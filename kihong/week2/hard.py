def solution(s):

    n = len(s)

    result = 0
    for start in range(n):
        for end in range(start + 1, n):
            if s[start] != s[end]:
                result += end - start
            else:
                s_part = s[start : end + 1]
                max_n = 0
                # 각 문장열 분석
                set_s = set(s_part)

                # reverse String 제작
                reverse_str = list(s_part)
                reverse_str.reverse()
                reverse_str = "".join(reverse_str)

                # 각 문자열에 대해서 큰 원소와 작은 원소 분석
                dict_s = {}
                for i in set_s:
                    dict_s[i] = [s_part.find(i), len(s_part) - reverse_str.find(i) - 1]

                # 각 원소에 대해서 큰 값 분석
                for item, value in dict_s.items():
                    for t_item, t_value in dict_s.items():
                        if item == t_item:
                            continue
                        max_n = max(
                            max_n,
                            abs(value[0] - t_value[1]),
                            abs(value[1] - t_value[0]),
                        )
                result += max_n

    return result


test_case = "baby"
test_case2 = "oo"

print(solution(test_case))


# 시간 복잡도 O(n^3)을 만들므로 폐기

# def beautiful(s_part: str):
#     # beautiful num
#     max_n = 0

#     # 문자열 길이
#     n = len(s_part)
#     if n == 1:
#         return 0

#     # 각 문장열 분석
#     set_s = set(s_part)

#     # reverse String 제작
#     reverse_str = list(s_part.strip())
#     reverse_str.reverse()
#     reverse_str = "".join(reverse_str)

#     # 각 문자열에 대해서 큰 원소와 작은 원소 분석
#     dict_s = {}
#     max_idx = 0
#     for i in set_s:
#         dict_s[i] = [s_part.find(i), n - reverse_str.find(i) - 1]
#     # 각 원소에 대해서 큰 값 분석
#     for item, value in dict_s.items():
#         for t_item, t_value in dict_s.items():
#             if item == t_item:
#                 continue
#             max_n = max(
#                 max_n, abs(value[0] - t_value[1]), abs(value[1] - t_value[0])
#             )
#     return max_n
