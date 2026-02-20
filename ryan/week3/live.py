def solution(number, k):
    my_stack = []
    
    for num in number:
        while my_stack and k and num > my_stack[-1]:
            my_stack.pop()
            k -= 1
        my_stack.append(num)

    if k > 0:
        my_stack = my_stack[:-k]

    return ''.join(my_stack)

print(solution("1924", 2))  # Output: "94"
print(solution("1231234", 3))  # Output: "3234"
print(solution("54321", 1))  # Output: "5432"