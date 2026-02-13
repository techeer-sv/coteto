class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int x = 0;
        int y = 0;

        for (int l : lottos) {
            if (l == 0) x++;
        }

        for (int i = 0; i < win_nums.length; i++) {
            for (int l : lottos) {
                if (l == win_nums[i]) {
                    y++;
                    break;
                }
            }
        }

        int happy = x + y;

        if (happy  < 2) happy = 1;
        if (y == 0) y = 1;

        return new int[] { 7 - happy, 7 - y };
    }
}
