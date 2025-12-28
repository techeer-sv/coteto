"""
1. 각 단어들을 돌아본다.
2. 만약 말할 수 있는 발음이 있다면 단어에서 그 발음을 한 번만 뺀다.
3. 나머지 발음 중에서 2번을 반복한다.
4. 만약 전 단어와 일치하거나, 더 이상 뺄 수 있는 단어가 없다면 반복을 그만둔다.
"""


def solution(babbling):
    can_words = ["aya", "ye", "woo", "ma"]
    answer = 0

    for word in babbling:
        current_word: str = word
        last_word = ""
        while current_word:
            found = False
            for can in can_words:
                if current_word.startswith(can) and can != last_word:
                    last_word = can
                    current_word = current_word[len(can) :]
                    found = True
            if not found:
                break
        if current_word == "":
            answer += 1

    return answer


babbling_case1 = ["aya", "yee", "u", "maa"]
babbling_case2 = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]

print(solution(babbling_case2))
