"""
각 열의 크기를 비교하면서 반복한다.
첫 번째 간격에서 만약
"""


def solution(s):
    import sys

    start_length = len(s)
    min_value = sys.maxsize

    for length in range(start_length, 0, -1):
        tmp = s[:length]
        tmp_str = ""

        sample_str = s[length:]
        cnt = 1

        while sample_str:
            if tmp == sample_str[:length]:
                cnt += 1
                sample_str = sample_str[length:]
            else:
                if cnt >= 2:
                    tmp_str += str(cnt) + tmp
                else:
                    tmp_str += tmp
                cnt = 1
                tmp = sample_str[:length]
                sample_str = sample_str[length:]

        tmp_str += tmp if cnt < 2 else str(cnt) + tmp
        min_value = min(len(tmp_str), min_value)

    answer = min_value
    return answer


test_case = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
]
for tc in test_case:
    print(solution(tc))
