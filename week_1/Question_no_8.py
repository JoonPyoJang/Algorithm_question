'''
문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

풀기전 생각하기
left 수와 right 수의 사이 값을 하나씩 함수에 넣는다.

함수 내용
n 의 숫자에서 1~n 까지의 숫자를 나눠 % = 0 인 수를 리스트에 저장한다. 이후 리스트의 길이가 짝수면 + 홀수면 -를 꼽한다.
'''
def solution(left, right):
    answer = 0
    def prime(num):
        list_num = [i for i in range(1,num+1) if num%i==0]
        num = num*-1 if len(list_num)%2 != 0 else num
        return num
    for i in range(left,right+1):
        answer = answer + prime(i)
    
    return answer

print(solution(13,17))