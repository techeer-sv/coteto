import java.util.*;
class Solution {
    public String[] solution(int[][] line) {

        List<List<Long>> list = new ArrayList<>();

        for (int i = 0; i < line.length; i++) {
            for (int j = i+1; j < line.length; j++) {
                long a = line[i][0] , b = line[i][1], c = line[i][2];
                long A = line[j][0], B = line[j][1], C = line[j][2];

                long inc = (a*B - A*b);

                if (inc == 0) continue;

                long xt = (C*b - c*B);
                long yt = (C*a - c*A);

                if (xt % inc != 0 || yt % inc != 0) continue;

                list.add(List.of(xt / inc, yt / inc));
            }
        }
        long maxX = Long.MIN_VALUE;
        long minX = Long.MAX_VALUE;
        long maxY = Long.MIN_VALUE;
        long minY = Long.MAX_VALUE;

        for (List<Long> l : list) {
            maxX = Math.max(maxX, l.get(0));
            minX = Math.min(minX, l.get(0));
            maxY = Math.max(maxY, l.get(1));
            minY = Math.min(minY, l.get(1));
        }

        int ylen = (int) (maxY - minY + 1);
        int xlen = (int) (maxX - minX + 1);

        String[] answer = new String[ylen];
        List<StringBuilder> temp = new ArrayList<>();
        for (int i = 0; i < ylen; i++) {
            StringBuilder s = new StringBuilder();
            for (int j = 0; j < xlen; j++) {
                s.append(".");
            }
            temp.add(s);
        }

        for (List<Long> l : list) {
            temp.get((int)(l.get(1) - minY))
                    .setCharAt((int)(l.get(0) - minX), '*');
        }

        for (int i = 0; i < temp.size(); i++) {
            answer[i] = temp.get(i).toString();
        }
        return answer;
    }
}
