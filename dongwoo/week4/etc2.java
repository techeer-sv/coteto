import java.util.*;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        int idx = 0;

        for (int i = 1; i <= order.length; i++) {
            stack.push(i);
            while (!stack.isEmpty() && order[idx] == stack.peek()) {
                stack.pop();
                answer++;
                idx++;
            }

        }
        return answer;
    }
}
