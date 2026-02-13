import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        LinkedList<Character> list = new LinkedList<>();
        for (char c : s.toCharArray()) {
            list.add(c);
        }

        for (int i = 0; i < list.size(); i++) {
            Deque<Character> stack = new ArrayDeque<>();
            boolean isPair = true;
            for (char c : list) {
                if (c == '[' || c == '(' || c == '{') {
                    stack.push(c);
                }
                else {
                    if (stack.isEmpty()) {
                        isPair = false;
                        break;
                    }
                    char top = stack.pop();
                    if (c == ']' && top != '[') {
                        isPair = false;
                        break;
                    }
                    if (c == ')' && top != '(') {
                        isPair = false;
                        break;
                    }
                    if (c == '}' && top != '{') {
                        isPair = false;
                        break;
                    }
                }
            }

            if (isPair && stack.isEmpty()) answer++;
            char temp = list.removeFirst();
            list.add(temp);
        }

        return answer;
    }
}
