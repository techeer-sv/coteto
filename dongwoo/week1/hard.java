import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> tc = new HashMap<>();
        Map<String, TreeSet<Integer>> pc = new HashMap<>();

        for (int i = 0; i<genres.length; i++) {
            tc.merge(genres[i], plays[i], Integer::sum);
            if (!pc.containsKey(genres[i])) {
                pc.put(genres[i], new TreeSet<>((k1, k2) -> {
                    int cmp = Integer.compare(plays[k2], plays[k1]);
                    return cmp != 0 ? cmp : Integer.compare(k1, k2);
                }));
            }
            pc.get(genres[i]).add(i);
        }

        List<String> sortedGenre = new ArrayList<>(tc.keySet());
        sortedGenre.sort((a,b) -> Integer.compare(tc.get(b), tc.get(a)));

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i<sortedGenre.size(); i++) {
            TreeSet<Integer> music = pc.get(sortedGenre.get(i));
            int musicCount = (music.size() >= 2) ? 2 : music.size();
            for (int j = 0; j<musicCount; j++) {
                result.add(music.pollFirst());
            }
        }

        return result.stream().
                mapToInt(Integer::intValue).toArray();
    }
}
