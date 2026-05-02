// lv2_의상
// https://school.programmers.co.kr/learn/courses/30/lessons/42578

class Solution {
    fun solution(clothes: Array<Array<String>>): Int {
        val map = HashMap<String, Int>()

        for (cloth in clothes) {
            val type = cloth[1]

            if (map.containsKey(type)) {
                map[type] = map[type]!! + 1
            } else {
                map[type] = 1
            }
        }

        var answer = 1

        for (key in map.keys) {
            val count = map[key]!!

            // (곱의법칙?)
            // 종류 중에 하나를 입는 경우 + 해당 종류를 아예 안 입는 경우 1
            answer *= count + 1
        }

        //  아무것도 안 입는 경우 제외
        return answer - 1
    }
}