'''
* 어떤 수치들을 입력받아 기본적인 통계량 4가지: 평균, 중앙값, 최빈값, 표준편차를 계산하는 프로그램을 작성하는 문제를 해결했는데,
* 몇몇 테스트케이스(예제 입력)에서 fail 하였다. 이유를 짐작해 보자.
* 문제 조건:
*   1.  해당 수치들은 모집단이다. 즉, 표준편차는 모표준편차를 구한다.
*   2.  평균은 산술평균을 구한다.
*   3.  최빈값은 데이터에서 등장한 빈도가 가장 높은 값을 의미한다.
		최빈값은 여러 개가 있을 수 있으나, 데이터의 모든 값이 최빈값인 경우(빈도가 같은 경우)에는 최빈값은 존재하지 않는다.
*   4.  중앙값은 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미한다.
		데이터가 짝수개인 경우 순서대로 정렬하였을 때 중앙의 두 값의 평균이 중앙값이 된다.
'''
from math import sqrt


def mean(data):  # 평균 구하기
	sum = 0
	for i in data:
		sum += i
	return sum / len(data)


def median(data): # 중앙값 구하기
	data.sort()
	if len(data)%2 == 0: # median이 짝수인경우 와 홀수인경우 다르게 계산.
		idx = len(data)//2
		return (data[idx] + data[idx-1])/2
	return data[len(data)//2]


def mode(data): # 최빈값 구하기
	mode_list = []
	freq = {}
	for i in data:
		try:
			freq[i] += 1
		except KeyError:
			freq[i] = 1
	max_value = max(freq.values())
	for key, value in freq.items():
		if value == max_value:
			mode_list.append(key)
	if set(mode_list) == set(data): # 데이터의 모든 값이 최빈값인 경우 최빈값은 존재하지 않는다.
		mode_list.clear()
	return mode_list


def std_dev(data):
	avg = mean(data)
	sum = 0
	for i in data:
		sum += (i - avg) ** 2
	return sqrt(sum/len(data))


input_data = list(map(int, input().split()))
print(f"평균: {mean(input_data)} 중앙값: {median(input_data)} 최빈값: {mode(input_data)} 표준편차: {std_dev(input_data)}")