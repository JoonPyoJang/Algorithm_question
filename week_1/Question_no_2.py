'''
문제 설명
정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

제한 조건
num은 int 범위의 정수입니다.
0은 짝수입니다.

풀기전 생각해보기
숫자를 받아 나눴을때 나머지가 0이면 짝수 아니면 홀수를 반환
'''
#급하게 제출한 정답
def solution(num):
    if num%2 ==0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer

#축약식 사용하여 간단하게 만들기
def solution2(num):
    answer = 'Even' if num%2 ==0 else 'Odd'
    return answer

