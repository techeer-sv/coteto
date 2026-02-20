def solution(wallpaper):
    min_x, min_y, max_x, max_y = 51, 51, -1, -1
    for i in range(len(wallpaper)):
        if wallpaper[i].count("#") == 0:
            continue
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                min_x, min_y, max_x, max_y = min(min_x, j), min(min_y, i), max(max_x, j+1), max(max_y, i+1)
            
    return [min_y, min_x, max_y, max_x]

print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))