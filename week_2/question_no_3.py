'''
문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한사항
n은 1이상 8000000000 이하인 자연수입니다.

풀기전 생각해보기
숫자를 리스트로 만들어 sort 함수를 써서 내림차순으로 정렬한다. 이후 리스트를 정수로 변환
'''

def solution(n):
    list = [i for i in str(n)]
    return int(''.join(sorted(list, reverse=True)))

print(solution(118372))