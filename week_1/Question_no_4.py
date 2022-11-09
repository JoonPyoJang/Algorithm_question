'''
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.

풀기전 생각하기
숫자를 입력받으면 문자열로 바꿔 뒤에서부터 리스트에 저장을 한다.

검색해본 함수 : 리스트 뒤집기
'''
# 급하게 입력한 코드
def solution(n):
    answer = []
    for i in str(n)[::-1]:
        answer.append(int(i))
    return answer

# 간단하게 풀어보기
def solution2(n):
    answer = [int(i) for i in str(n)[::-1]]
    return answer
