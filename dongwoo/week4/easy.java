class Solution {
    public int solution(int[] array) {
        int answer = 0;
        for (int a : array) {
            for (char c : String.valueOf(a).toCharArray()) {
                if (c == '7') {
                    answer++;
                }
            }
        }
        return answer;
    }
}
