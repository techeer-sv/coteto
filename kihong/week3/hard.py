# 맞는 숫자와 틀린 숫자에 따라서 최고 등수와 최저 등수를 선택할 수 있다.
# 고로 미리 선택된 값에 따라 비교하여 최고 등수와 최저 등수를 찾아본다.
def solution(lottos: list, win_nums):

    may_num = 0
    true_num = 0
    for num in lottos:
        if num in win_nums:
            true_num += 1
        elif num == 0:
            may_num += 1
    may_num += true_num
    answer = []
    greatest_rank = 7 - may_num if 7 > 7 - may_num > 0 else 6
    answer.append(greatest_rank)
    lowtest_rank = 7 - true_num if 7 > 7 - true_num > 0 else 6
    answer.append(lowtest_rank)
    return answer


def main():
    cases = [
        {
            "lottos": [44, 1, 0, 0, 31, 25],
            "win_nums": [31, 10, 45, 1, 6, 19],
            "result": [3, 5],
        },
        {
            "lottos": [0, 0, 0, 0, 0, 0],
            "win_nums": [38, 19, 20, 40, 15, 25],
            "result": [1, 6],
        },
        {
            "lottos": [45, 4, 35, 20, 3, 9],
            "win_nums": [20, 9, 3, 45, 4, 35],
            "result": [1, 1],
        },
        {
            "lottos": [1, 1, 1, 1, 1, 1],
            "win_nums": [20, 9, 3, 45, 4, 35],
            "result": [6, 6],
        },
    ]
    for i, tc in enumerate(cases):
        result = solution(tc["lottos"], tc["win_nums"])
        assert (
            result == tc["result"]
        ), f"failed user_result : {result} true_result : {tc["result"]}"
        print(f"[{i}] success")


if __name__ == "__main__":
    main()
