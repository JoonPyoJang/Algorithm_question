'''
문제 설명
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

제한사항
N의 범위 : 100,000,000 이하의 자연수

풀기전 생각해보기
자리수를 더하기 위해서는 먼저 str 타입으로 바꿔 리스트 형태로 만들어 각각 더해주면 된다.

for 문을 사용하기는 했는데 분명 다른 방법이 있었는데 생각이 안난다...
'''

#급하게 제출한 정답
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer

#간단하게 풀어보기
def solution2(n):
    
    answer = [int(i) for i in str(n)]

    return sum(answer)

