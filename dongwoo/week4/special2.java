class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr2[0].length];
        int x = arr1.length;
        int y = arr1[0].length;
        int p = arr2.length;
        int k = arr2[0].length;

        for (int i = 0; i < x; i++) {
            for (int j = 0; j < k; j++) {
                int t = 0;
                for (int u = 0; u < y; u++) {
                    t += (arr1[i][u] * arr2[u][j]);
                }
                answer[i][j] = t;
            }
        }
        return answer;
    }
}
