import requests
response=requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&lang="+"en"+"&format=json")
print(response.status_code)
print(response.content)
