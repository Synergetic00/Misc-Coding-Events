import requests
from bs4 import BeautifulSoup
import re

URL = 'http://challenges.neverlanctf.com:1240/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
text = list(set(soup.find_all(text=True)))

for element in text:
    if "+" in element:
        result = element

equation = re.sub('\s+', '', result).split("+")

add = int(equation[0]) + int(equation[1])

print(add)

newUrl = "http://challenges.neverlanctf.com:1240/?submitted"
data = {'answer':add}
response = requests.post(newUrl,data=data)
print(response.text)