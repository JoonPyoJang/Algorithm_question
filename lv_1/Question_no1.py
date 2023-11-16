'''
문제 설명
얀에서는 매년 달리기 경주가 열립니다. 
해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 
예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 
해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 
즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.
선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 
players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 
경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.

제한사항
5 ≤ players의 길이 ≤ 50,000
players[i]는 i번째 선수의 이름을 의미합니다.
players의 원소들은 알파벳 소문자로만 이루어져 있습니다.
players에는 중복된 값이 들어가 있지 않습니다.
3 ≤ players[i]의 길이 ≤ 10
2 ≤ callings의 길이 ≤ 1,000,000
callings는 players의 원소들로만 이루어져 있습니다.
경주 진행중 1등인 선수의 이름은 불리지 않습니다.

생각적어보기
1. players 리스트에서 calling에 이름이 불리면 player 리스트의 이름을 한칸 앞으로 보낸다.
2. for 문으로 calling에 리스트를 돌리고 해당 player를 앞으로 보낸다.

느낀점
리스트에서 해당 인덱스를 찾는건 리스트의 길이만큼의 시간이 계속 들지만 딕셔너리로 만들고 딕셔너리에서 해당 위치를 찾는건 훨씬 빨라
내가 처음에 짠 코드에서는 시간이 오래 걸린듯하다. index = players.index(i)이 줄이 for 문에서 돌아갔을때 리스트 길이 만큼 제곱으로 돌아가는 수준
따라서 시간초과가 나온거 같다. 링크드리스트와 배열의 차이인듯 하다.

'''
# 내가 짠 코드 (시간초과)
def solution(players, callings):
    for i in callings:
        index = players.index(i)
        if index > 0 :
            players[index-1], players[index] = players[index], players[index-1]
    return players

# 수정한 코드
def solution(players, callings):
    result = {player: i for i, player in enumerate(players)}
    for i in callings:
        index = result[i]
        result[i] -= 1
        result[players[index-1]] += 1
        players[index-1], players[index] = players[index], players[index-1]
    return players


players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["mumu","kai", "kai", "mine", "mine"]
solution(players, callings)