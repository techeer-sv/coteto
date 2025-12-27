def is_ok(word):
    sounds = ["aya", "ye", "woo", "ma"]
    last = ""
    rest = word

    while rest:
        matched = False

        for s in sounds:
            if rest.startswith(s):
                if s == last:      
                    return False
                last = s
                rest = rest[len(s):]
                matched = True
                break

        if not matched:           
            return False

    return True


def solution(babbling):
    answer = 0
    for word in babbling:
        if is_ok(word):
            answer += 1
    return answer
