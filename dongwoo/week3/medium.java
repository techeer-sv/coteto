class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        int count = 0;
        int glen = goal.length;
        int p1 = 0;
        int p2 = 0;
        while (count < glen) {
            String g = goal[count];
            if (p1 < cards1.length) {
                if (g.equals(cards1[p1])) {
                    p1++;
                    count++;
                    continue;
                }
            }
            if (p2 < cards2.length) {
                if (g.equals(cards2[p2])) {
                    p2++;
                    count++;
                    continue;
                }
            }

            return "No";

        }
        return answer;
    }
}
