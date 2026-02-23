import java.util.*;

class Solution {
    int solution(int[][] land) {
        int answer = 0;

        for (int i = 1; i < land.length; i++) {
            for (int j = 0; j < 4; j++) {
                int temp = 0;
                for (int z = 0; z < 4; z ++) {
                    if (j != z) {
                        temp = Math.max(temp, land[i-1][z]);
                    }
                }
                land[i][j] += temp;
            }
        }

        for (int l : land[land.length-1]) {
            answer = Math.max(l, answer);
        }

        return answer;
    }
}
