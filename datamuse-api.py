import requests

param = {'rel_rhy': 'jingle'}
result = requests.get('https://api.datamuse.com/words', param).json()
array_words = []
for i in result:
    array_words.append(i['word'])

array_words.sort()          # ASC Order
# array_words.sort(reverse=True)   #DESC Order
print(array_words)