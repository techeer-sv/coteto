class Solution {
    public String solution(String rsp) {
        String answer = "";
        for (char r : rsp.toCharArray()) {
            if (r == '2') answer += '0';
            if (r == '0') answer += '5';
            if (r == '5') answer += '2';
        }
        return answer;
    }
}
