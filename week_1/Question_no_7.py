'''
비밀지도
네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.

지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.
전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 "지도 1"과 "지도 2"라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
"지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.
암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

풀기전 생각하기
배열에 나오는 데이터를 이진수로 바꿔 두개 데이터를 더해 구한다. 만약 자리수가 없다면 0을 채운다.
'''
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = format(arr1[i], 'b')
        b = format(arr2[i], 'b')

        if len(a) < n:
            num = n - len(a)
            a = '0'*num + a

        if len(b) < n:
            num = n - len(b)
            b = '0'*num + b

        key = ''
        for j in range(n):
            if a[j] == '1' or b[j] =='1':
                key += '1'
            else:
                key += '0'
        key = key.replace("1","#")
        key = key.replace("0"," ")
        answer.append(key)
    
    return answer



print(bin(7)[2:].zfill(5))
# 무조건 번지수까지 빈칸을 채운다 만약 010에 5를 쓰면 앞에 00을 채워 00010으로 만든다.

