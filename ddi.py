import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize, sent_tokenize
import csv
from gensim.models import Word2Vec
import pandas as pd
from docx import Document



"""
url = "https://www.skysports.com/f1/news"

istek_one = requests.get(url)
içerikler = istek_one.content
soup_one = BeautifulSoup(içerikler, "html.parser")

divTag = soup_one.find_all("div", {"class": "news-list__item news-list__item--show-thumb-bp30"})

links = []
for divTag in soup_one.find_all("h4", {"class": "news-list__headline"}):
    aTag = divTag.find('a')
    links.append(aTag.get('href'))

haberler_tokenize = []

x = 0
y = 0

for link in links:
    istek_two = requests.get(link)
    soup_two = BeautifulSoup(istek_two.content, "html.parser")
    haber_icerik = soup_two.find_all("span", {"class": "article__long-title"})

    for p in haber_icerik:
        haberler_tokenize.append(sent_tokenize(p.text))

csv_file = open("ddivizeödev.csv", "w")
file_writer = csv.DictWriter(csv_file, fieldnames=['url', 'segment_no', 'cumle_icerigi', 'sozcuk_sayisi'])
file_writer.writeheader()
for q in range(0, len(haberler_tokenize)):
    for w in range(0, len(haberler_tokenize[q])):
        kelime = word_tokenize(haberler_tokenize[q][w])
        file_writer.writerow(
            {'url': links[q], 'segment_no': w, 'cumle_icerigi': haberler_tokenize[q][w], 'sozcuk_sayisi': len(kelime)})
        x = x + 1
csv_file.close()
"""

#Üst kısım vize ödevi ile alakalıdır.

dataframe=pd.read_csv("ddivizeödev.csv")
newsTitles=dataframe['cumle_icerigi'].values
for newsvec in newsTitles:
    word_tokenize(newsvec)
    print(newsvec)
model=Word2Vec([newsvec],min_count=1,size=32)
vec=model.wv['a']-model.wv['v']+model.wv['b']
similarity=model.wv.most_similar([vec])

"""doc=Document()
doc.add_paragraph(similarity)     #Hocam docx dosyasına veri aktaramadım o yuzden txt dosyasına yazdırdım
doc.save("Word2Vec.docx")"""



with open('Word2Vec.txt','w') as f:
    for item in similarity:
        f.write(str(item)+'\n')













