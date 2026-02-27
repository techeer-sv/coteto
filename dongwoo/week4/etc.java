import java.util.*;
class Solution {
    int solution(int[][] land) {
        int answer = 0;
        for (int i = 1; i < land.length; i++) {
            for (int j = 0; j < 4; j++) {
                int max = 0;
                for (int x = 0; x < 4; x++) {
                    if (x != j) {
                        max = Math.max(max, land[i-1][x]);
                    }
                }
                land[i][j] += max;
            }
        }
        Arrays.sort(land[land.length-1]);
        return land[land.length-1][3];
    }
}
