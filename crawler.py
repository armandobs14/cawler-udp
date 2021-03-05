import requests
from bs4 import BeautifulSoup

url = "https://acoescoronavirus.uniaodospalmares.al.gov.br"
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text)
boxes = soup.find_all("div", {"class": "single-counter-box"})

info = dict()
for box in boxes:
    key = box.p.text
    value = int(box.h1.span.text)
    info[key] = value

print(info)
