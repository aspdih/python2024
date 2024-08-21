import requests
#serviceKey='Zb%2BjR%2B3GmNkj%2BvESTcV7DarlLIm37YTauUkem3YJ%2FOpxmTwitYgkBaV8QjDoddZibcsvAtYVrhaoxoCjsmW4mw%3D%3D'
servicekey='Zb+jR+3GmNkj+vESTcV7DarlLIm37YTauUkem3YJ/OpxmTwitYgkBaV8QjDoddZibcsvAtYVrhaoxoCjsmW4mw=='
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' : servicekey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '서울', 'ver' : '1.0' }

response = requests.get(url, params=params)
print(response.content)