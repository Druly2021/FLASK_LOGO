import requests


res = requests.get("http://numbersapi.com/08/03/date")
print(res.text)
