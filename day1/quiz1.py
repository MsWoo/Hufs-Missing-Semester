'''
* 두 정수 a, b를 입력받고, a+b를 출력 후 반복. a와 b가 둘 다 0인경우 프로그램 종료!
'''

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)
