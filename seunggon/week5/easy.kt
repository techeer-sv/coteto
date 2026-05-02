// lv2_피보나치수
// https://school.programmers.co.kr/learn/courses/30/lessons/12945?language=kotlin

class Solution {
    fun solution(n: Int): Int {
        val dp = IntArray(n + 1)

        dp[0] = 0
        dp[1] = 1

        for (i in 2..n) {
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
        }

        return dp[n]
    }
}