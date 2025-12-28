def solution(s: str):
    s_list: list = []

    is_space = True

    # 공백도 포함해서 리스트화하는 과정
    while s:
        idx = 0
        while True:
            # 마지막 인덱스까지 고려해서 list화
            if is_space and (idx == len(s) or s[idx].isspace()):
                s_list.append(s[:idx])
                s = None if idx == len(s) else s[idx:]
                is_space = False
                break
            elif not is_space and (idx == len(s) or not s[idx].isspace()):
                s_list.append(s[:idx])
                s = s[idx:]
                is_space = True
                break
            idx += 1

    result = []
    for word in s_list:
        if word[0].isdigit():
            result.append(word[0] + word[1:].lower())
        elif word.isspace():
            result.append(word)
        else:
            result.append(word[0].upper() + word[1:].lower())

    answer = "".join(result)
    return answer


test_case = "3people        4unFollowed me    "
test_case_1 = "for the last week"

print(solution(test_case))
print(solution(test_case_1))
