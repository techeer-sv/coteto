# (정렬 lv2.) 가장 큰 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

# 라이브로 풀 때 버블 정렬(O(N^2)을 작성해서 풀었는데 시간 초과가 나서 퀵 정렬(O(NlogN))로 다시 풀었더니 통과
# 궁금증) 파이썬 sort로 푼다면 lambda에 뭘 지정해야 하는 지 모르겠음...
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]    
    left = []         
    right = []       
    
    for item in arr[1:]:
        if item + pivot > pivot + item:
            left.append(item)
        else:                  
            right.append(item)
            
    return quick_sort(left) + [pivot] + quick_sort(right)

def solution(numbers):
    str_numbers = [str(n) for n in numbers]
    
    sorted_numbers = quick_sort(str_numbers)
    
    answer = "".join(sorted_numbers)
    
    if answer[0] == '0':
        answer = '0'

    
    return answer