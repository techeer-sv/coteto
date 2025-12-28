def solution(babbling):
    answer = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        i = 0
        prev = ""
        ok = True

        while i < len(word):
            matched = False

            for s in answer:
                if word.startswith(s, i):
                    if prev == s:
                        ok = False
                        matched = True
                        break
                    prev = s
                    i += len(s)
                    matched = True
                    break

            if not ok:
                break
            if not matched:
                ok = False
                break

        if ok:
            count += 1

    return count
