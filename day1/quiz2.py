'''
* n개로 이루어진 수열 A가 있다. 이 때, 수열 A에서 정수 x보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
* 입력으로는 첫째 줄에서 수열의 길이와 x, 둘째 줄에서 수열의 길이만큼의 정수가 입력된다.
* 입력 예시:
*   5 3
*   10 2 6 -7 5
* 출력 예시:
*   2 -7
'''

n, x = tuple(map(int, input().split()))

A = list(map(int, input().split()))
    
answer = []

for ele in A:
    if ele < x:
        answer.append(ele)

for i in range(len(answer)):
    print(answer[i], end=" ")