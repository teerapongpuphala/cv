import requests
from bs4 import BeautifulSoup
import re
# url = "https://www.healthline.com/nutrition/protein-in-egg"
# url = "https://www.mensjournal.com/food-drink/30-ways-get-30-grams-protein-every-meal/breakfast-6/"
url="https://healthyeating.sfgate.com/much-protein-egg-5739.html"
response = requests.get(url,verify = False)
soup = BeautifulSoup(response.content, "html.parser")
textT = soup.find_all(text=True)

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'style'
    # there may be more elements you don't want, such as "style", etc.
]

for t in textT:
    if t.parent.name not in blacklist:
        t=re.sub('\n',' ',t)
        t=re.sub('\t','',t)
        output += '{} '.format(t)

# print(output)
wordsList = output.strip().split(' ')
print(set(wordsList))