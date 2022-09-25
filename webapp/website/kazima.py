import requests
from bs4 import BeautifulSoup
r=requests.get("http://www.koeri.boun.edu.tr/scripts/lst7.asp")
soup =BeautifulSoup(r.content,"html.parser")
tumkelimeler = soup.find_all("pre")
for kelimegruplari in soup.find_all("pre"):
    icerik= kelimegruplari.text
    print (icerik)
print(tumkelimeler)