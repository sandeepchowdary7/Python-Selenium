import requests

result = requests.get('http://api.open-notify.org/astros.json').json()
for p in result['people']:
    print(p['name'])
