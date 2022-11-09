'''
문제 설명
0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

풀기전 생각하기
0~9 까지에 수와 입력된 list를 집합으로 만들어 차집합을 하고 나온 결과를 더한다.
'''

def solution(numbers):

    answer_list = set(range(10)) - set(numbers)

    answer = sum(answer_list)
    return answer


numbers = [5,8,4,0,6,7,9]
print(solution(numbers))