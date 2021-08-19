import requests
import xmltodict
import pandas as pd

url_base = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson"
serviceKey = "" #your key
pages = "100"
start_date = "20210801"
end_date = "20210819"
url = f"{url_base}?serviceKey={serviceKey}&pageNo=1&numOfRows={pages}&startCreateDt={start_date}&endCreateDt={end_date}"

response = requests.get(url).content

xmltodictObject = xmltodict.parse(response)
dict_data = xmltodictObject['response']['body']['items']['item']

data_frame = pd.DataFrame(dict_data)
data_frame = data_frame.astype({'decideCnt' : 'int', 'examCnt' : 'int', 'deathCnt' : 'int'})
data_frame = data_frame.drop_duplicates(['stateDt'])
data_frame['date'] = data_frame['stateDt']
data_frame['date'] = pd.to_datetime(data_frame['date'])
data_frame.set_index('date')

data_frame_2 = data_frame[['date','decideCnt','examCnt','deathCnt']]
data_frame_2 = data_frame_2.sort_values(by='date')
data_frame_2['daily_confirmedCases'] = data_frame_2['decideCnt'].diff()
data_frame_2.plot('date', ['daily_confirmedCases'])