import requests


res = requests.get("http://numbersapi.com/<number>/<type>")
print(res.text)