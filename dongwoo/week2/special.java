import java.util.*;
class Solution {
    public int solution(String s) {
        int len = s.length();
        int hlen = len / 2;
        int answer = len;
        for (int i = 1; i <= hlen; i++) {
            StringBuilder sb = new StringBuilder();
            String prev = s.substring(0, i);
            int count = 1;
            for (int j = i; j < len; j += i) {
                String cur = "";
                if (i + j > len) {
                    cur = s.substring(j);
                } else cur = s.substring(j, i + j);

                if (prev.equals(cur)) {
                    count++;
                } else {
                    if (count > 1) {
                        sb.append(count);
                    }
                    sb.append(prev);
                    prev = cur;
                    count = 1;
                }
            }
            if (count > 1) {
                sb.append(count);
            }
            sb.append(prev);
            answer = (answer > sb.length()) ? sb.length() : answer;
        }

        return answer;
    }
}
