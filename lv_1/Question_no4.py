'''
문제 설명
컴퓨터 바탕화면은 각 칸이 정사각형인 격자판입니다. 
이때 컴퓨터 바탕화면의 상태를 나타낸 문자열 배열 wallpaper가 주어집니다. 
파일들은 바탕화면의 격자칸에 위치하고 바탕화면의 격자점들은 바탕화면의 가장 왼쪽 위를 (0, 0)으로 시작해 
(세로 좌표, 가로 좌표)로 표현합니다. 빈칸은 ".", 파일이 있는 칸은 "#"의 값을 가집니다. 
드래그를 하면 파일들을 선택할 수 있고, 선택된 파일들을 삭제할 수 있습니다. 
머쓱이는 최소한의 이동거리를 갖는 한 번의 드래그로 모든 파일을 선택해서 한 번에 지우려고 하며 
드래그로 파일들을 선택하는 방법은 다음과 같습니다.

머쓱이의 컴퓨터 바탕화면의 상태를 나타내는 문자열 배열 wallpaper가 매개변수로 주어질 때 
바탕화면의 파일들을 한 번에 삭제하기 위해 최소한의 이동거리를 갖는 
드래그의 시작점과 끝점을 담은 정수 배열을 return하는 solution 함수를 작성해 주세요. 
드래그의 시작점이 (lux, luy), 끝점이 (rdx, rdy)라면 정수 배열 [lux, luy, rdx, rdy]를 return하면 됩니다.

제한사항
1 ≤ wallpaper의 길이 ≤ 50
1 ≤ wallpaper[i]의 길이 ≤ 50
wallpaper의 모든 원소의 길이는 동일합니다.
wallpaper[i][j]는 바탕화면에서 i + 1행 j + 1열에 해당하는 칸의 상태를 나타냅니다.
wallpaper[i][j]는 "#" 또는 "."의 값만 가집니다.
바탕화면에는 적어도 하나의 파일이 있습니다.
드래그 시작점 (lux, luy)와 끝점 (rdx, rdy)는 lux < rdx, luy < rdy를 만족해야 합니다.

생각해보기
가장 왼쪽에 있는 좌표, 가장 오른쪽에 있는 좌표, 가장 위 아래에 있는 좌표를 구한 후 사각형으로 넢는다
'''

wallpaper = [".#...", "..#..", "...#."]
def solution(wallpaper):
    point = []
    sx, sy, bx, by = 50, 50, 0, 0
    x,y = len(wallpaper[0]), len(wallpaper)
    for j in range(x):
        for i in range(y):
            if wallpaper[i][j] == '#':
                #sx 최소 값 저장하기
                print(i,j)
                if sx > i: sx = i
                if sy > j: sy = j
                if bx <= i: bx = i+1
                if by <= j: by = j+1
                print(sx, sy, bx, by)
    
    return [sx, sy, bx, by]


print(solution(wallpaper))
        

