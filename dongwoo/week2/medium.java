import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        String[] splits = s.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i<splits.length; i++) {
            String lower = splits[i].toLowerCase();
            if (!lower.isEmpty())
                lower = Character.toUpperCase(lower.charAt(0)) + lower.substring(1);
            sb.append(lower);
            if (i<splits.length-1)
                sb.append(" ");
        }

        return sb.toString();
    }
}
