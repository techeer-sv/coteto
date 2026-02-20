import java.util.*;
class Solution {
    public int[] solution(int n) {

        int[] dx = {0, 1, -1};
        int[] dy = {1, 0, -1};

        int[][] temp = new int[n][n];
        int max = n * (n+1) / 2;

        int x = 0;
        int y = 0;
        int num = 1;
        int dir = 0;
        for (int i = 0; i < max; i++) {
            temp[y][x] = num;
            num++;
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (nx >= n || ny >= n || nx < 0 || ny < 0 || temp[ny][nx] != 0) {
                dir = (dir + 1) % 3;
                nx = x + dx[dir];
                ny = y + dy[dir];
            }

            x = nx;
            y = ny;
        }

        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                answer.add(temp[i][j]);
            }
        }
        return answer.stream().mapToInt(i->i).toArray();
    }
}
