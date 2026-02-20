def solution(rsp):
    result = ""
    for input in rsp:
        if input == "2":
            result += "0"
        elif input == "0":
            result += "5"
        else:
            result += "2"
    answer = result
    return answer


def main():
    cases = [{"input": "2", "output": "0"}, {"input": "205", "output": "052"}]
    for i, tc in enumerate(cases):
        result = solution(tc["input"])
        assert (
            result == tc["output"]
        ), f"[{i}] 실패: expected={tc["output"]} output={result}"
        print(f"[{i}] 통과")


if __name__ == "__main__":
    main()
