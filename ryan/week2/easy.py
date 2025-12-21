def solution(babbling):
    answer = 0
    
    for i in range(len(babbling)):
        flag = True
        type_ongal = 0
        babble = babbling[i]
        if "aya" in babble:
            type_ongal += 1
            babble = babble.replace("aya", "!")
            if "!!" in babble:
                flag = False
        if "ye" in babble:
            type_ongal += 1
            babble = babble.replace("ye", "@")
            if "@@" in babble:
                flag = False
        if "woo" in babble:
            type_ongal += 1
            babble = babble.replace("woo", "#")
            if "##" in babble:
                flag = False
        if "ma" in babble:
            type_ongal += 1
            babble = babble.replace("ma", "$")
            if "$$" in babble:
                flag = False
        if type_ongal > 0 and flag:
            if len(set(babble)) == type_ongal:
                answer += 1
        
    return answer