def solution(number, k):
    result = []
    for n in number:
        while result and k and result[-1] < n:
            result.pop()
            k -= 1
        result.append(n)
    if k > 0:
        result = result[:-k]

    result = "".join(result)
    return result


def main():
    cases = [
        # {"number": "1924", "k": 2, "return": "94"},
        # {"number": "4177252841", "k": 4, "return": "775841"},
        {"number": "42", "k": 1, "return": "4"},
    ]
    for i, tc in enumerate(cases):
        result = solution(tc["number"], tc["k"])
        if result != tc["return"]:
            print(f"내 꺼 : {result} 정답 : {tc["return"]}")
        else:
            print(f"{i}번째 맞았음.")


if __name__ == "__main__":
    main()
