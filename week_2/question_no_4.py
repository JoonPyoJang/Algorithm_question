'''
문제 설명
자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

제한사항
3 ≤ n ≤ 1,000,000

풀기전 생각해보기
n 번째까지 리스트를 만들어 for 문으로 돌리고, for 문내 if 문을 사용해 나머지가 1이면 return 을 해준다.
'''

def solution(n):
    for i in range(1, n):
        if n%i == 1:
            return i
    
print(solution(12))