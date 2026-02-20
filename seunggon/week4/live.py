# 바탕화면 정리
# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):

    x_list = []
    y_list = []

    for r,i in enumerate(wallpaper):
        temp = i.find("#")
        while (temp != -1):
            x_list.append(temp)
            y_list.append(r)
            i = i[:temp] + "." + i[temp+1:]
            # print(i)
            temp = i.find("#")
    answer = [
        min(y_list), 
        min(x_list), 
        max(y_list) + 1, 
        max(x_list) + 1
    ]

    return answer