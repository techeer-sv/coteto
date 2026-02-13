def solution(s):
    n = len(s)
    s = s + s[:-1]
    ans = 0
    for i in range(n):
        part = s[i:n+i]
        my_stack = []
        for j in part:
            if j == "[":
                my_stack.append("[")
            elif j == "]":
                if len(my_stack) > 0 and my_stack[-1] == "[":
                    my_stack.pop()
                else:
                    my_stack.append("]")
                    break
            elif j == "(":
                my_stack.append("(")
            elif j == ")":
                if len(my_stack) > 0 and my_stack[-1] == "(":
                    my_stack.pop()
                else:
                    my_stack.append(")")
                    break
            elif j == "{":
                my_stack.append("{")
            elif j == "}":
                if len(my_stack) > 0 and my_stack[-1] == "{":
                    my_stack.pop()
                else:
                    my_stack.append("}")
                    break
        if not my_stack:
            ans += 1
    return ans

solution("[](){}")
solution("}]()[{")