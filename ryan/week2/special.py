def solution(s):
    length_ans = len(s)
    for i in range(1, len(s) // 2 + 1):
        ans = ''
        part = s[0:i]
        count = 1
        for j in range(i, len(s), i):
            if part == s[j:j + i]:
                count += 1
            else:
                if count > 1:
                    ans += str(count) + part
                else:
                    ans += part
                part = s[j:j + i]
                count = 1
        if count > 1:
            ans += str(count) + part
        else:
            ans += part
        length_ans = min(len(ans), length_ans)
    return length_ans

# n^2 실화냐