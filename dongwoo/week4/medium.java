import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        int[] one = {1, 2, 3, 4, 5};
        int[] two = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] thr = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] result = {0,0,0};
        for (int i = 0; i < answers.length; i++) {
            int t = answers[i];
            if (one[i%5] == t) {
                result[0] += 1;
            }
            if (two[i%8] == t) {
                result[1] += 1;
            }
            if (thr[i%10] == t) {
                result[2] += 1;
            }
        }

        int top = 0;
        for (int i : result) {
            if (i > top) top = i;
        }

        for (int i = 0; i < 3; i++) {
            if (top == result[i]) answer.add(i+1);
        }

        return answer.stream().mapToInt(i->i).toArray();
    }
}
