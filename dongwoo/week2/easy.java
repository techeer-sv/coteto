class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] rrr = {"aya", "ye", "woo", "ma"};
        for (String s : babbling) {
            if (s.contains("ayaaya") || s.contains("yeye") || s.contains("woowoo") || s.contains("mama")) {
                continue;
            }

            for (String r : rrr) {
                s = s.replace(r, " ");
            }

            if (s.trim().length() == 0) {
                answer++;
            }
        }
        return answer;
    }
}
