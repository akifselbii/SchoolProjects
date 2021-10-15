#Mehmet Akif SELBİ

import requests
from bs4 import BeautifulSoup

def site_linki():
    r = requests.get('http://ce.muhendislik.comu.edu.tr/arsiv/duyurular')
    source = BeautifulSoup(r.content,"html.parser")

    return source
    
def linkler():
    #linkler
    source = site_linki()
    source_link = source.find_all("a")
    flag=0
    d_link=[]
    for i in source_link:
        if(i.text == "Duyurular"):flag = 1
        if(i.text == "İlk"):flag = 0
        if(flag == 1):
            if(i.get("href")!= "arsiv/duyurular"):
                d_link.append("http://ce.muhendislik.comu.edu.tr"+i.get("href"))
    return d_link

def basliklar():
    #tablodaki başlıklar
    d_title=[]
    source = site_linki()
    source_title = source.find_all("td")
    for i in source_title:
        d_title.append(i.text)
    return d_title

def yazilar(d_link):
    #link sayfalarındaki yazıları çekmek için
    d_link_text=[]
    for i in range(len(d_link)):
        r = requests.get(d_link[i])
        source = BeautifulSoup(r.content,"html.parser")
        source_link = source.find_all("p")
        dizi=[]
        for j in source_link:
            dizi.append(j.text)
        yazi = dizi[1]
        if "Paylaş" in yazi:
            yazi = yazi.replace("Paylaş","")
        d_link_text.append((yazi+"\nDuyuru Linki : "+d_link[i]))
        
    return d_link_text

