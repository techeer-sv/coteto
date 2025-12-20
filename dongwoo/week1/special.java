import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        char[][] types = {{'R', 'T'}, {'C', 'F'}, {'J', 'M'}, {'A', 'N'}};
        // RT TR
        // CF FC
        // JM MJ
        // AN NA
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < survey.length; i++) {
            int cv = choices[i];
            if (cv < 4) {
                cv = 4 - cv;
                map.put(survey[i].charAt(0), map.getOrDefault(survey[i].charAt(0), 0) + cv);
            }
            else if (cv > 4) {
                cv = cv - 4;
                map.put(survey[i].charAt(1), map.getOrDefault(survey[i].charAt(1), 0) + cv);
            }
        }

        for (int i = 0; i < 4; i++) {
            char f = types[i][0];
            char s = types[i][1];
            int fc = map.getOrDefault(f, 0);
            int sc = map.getOrDefault(s, 0);

            if (fc >= sc)  answer += f;
            else answer +=s;
        }

        return answer;
    }
}
